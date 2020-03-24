from unittest import skip
from unittest.mock import patch, MagicMock

import numpy as np
from flask_testing import TestCase

from myapp.main import create_app
from myapp.main.cats.cat_dao import CatDAO
from myapp.main.cats.cats_service import CatService
from myapp.main.model.cat_model import CatParentDO, CatDO


class CatServiceTest(TestCase):
    """
    Test class testing the Cat Service class
    """

    def create_app(self):
        """
        Create Dummy App for working
        :return: app
        """
        app = create_app('dev')
        app.config['TESTING'] = True
        return app

    @patch("myapp.main.cats.cat_dao.CatDAO.find_by_age")
    def test_get_cats(self, mock_find_by_age):
        """
        Test using Patching decorator
        :param mock_find_by_age:
        :return: None
        """

        parent = CatParentDO('Meow Parent1', 'M')
        cat = CatDO('Meow 1', 1, parent)
        # when call goes to this method return some dummy value
        mock_find_by_age.return_value = [cat]

        mycat_ser = CatService()
        resp = mycat_ser.get_cats(2)

        # traditional checks
        assert resp.description == "This is list of cats"
        assert resp.no_of_cats == 1

        # checks if mock was called
        mock_find_by_age.assert_called_with(2)

        # from below use the appropriate one for above assert
        # assert_called()
        # assert_called_with
        # assert_called_once_with
        # assert_any_call
        # assert_has_calls
        # assert_not_called

    @staticmethod
    def test_get_cats1():
        """
        Test Using MagicMock
        :return: None
        """
        parent = CatParentDO('Meow Parent1', 'M')
        cat = CatDO('Meow 1', 1, parent)
        # when call goes to this method, return some dummy value
        CatDAO.find_by_age = MagicMock(return_value=[cat])
        resp = CatService.get_cats(1)

        # traditional checks
        assert resp.description == "This is list of cats"
        assert resp.no_of_cats == 1

        # checks if mock was called  and how
        CatDAO.find_by_age.assert_called_once_with(1)

    @skip("correct it later")
    def test_how_to_ignore(self):
        a = np.array([[1, 1]])

        print(a.shape)
        a = np.squeeze(a)
        print(a, a.shape)
