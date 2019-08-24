from unittest import skip
from unittest.mock import patch, MagicMock

from flask_testing import TestCase

from myapp.main import create_app
from myapp.main.cats.cats_service import CatService
from myapp.main.model.cat_model import CatParentDO, CatDO


class CatServiceTest(TestCase):

    def create_app(self):
        app = create_app('dev')
        app.config['TESTING'] = True
        return app

    @patch("myapp.main.cats.cats_service.CatService._create_dummy_cats")
    def test_get_cats(self, mock_create_dummy_cats):
        """
        Using Patching a method
        :param mock_create_dummy_cats:
        :return: None
        """
        mycat_ser = CatService()
        parent = CatParentDO('Meow Parent1', 'M')
        cat = CatDO('Meow 1', 1, parent)
        # when call goes to this method return some dummy value
        mock_create_dummy_cats.return_value = [cat]
        resp = mycat_ser.get_cats()
        assert resp.description == "This is list of cats"
        mock_create_dummy_cats.assert_called_once()

    @staticmethod
    def test_get_cats1():
        """
        Using MagicMock
        :return: None
        """
        parent = CatParentDO('Meow Parent1', 'M')
        cat = CatDO('Meow 1', 1, parent)
        # when call goes to this method, return some dummy value
        CatService._create_dummy_cats = MagicMock(return_value=[cat])
        resp = CatService.get_cats()
        assert resp.description == "This is list of cats"
        CatService._create_dummy_cats.assert_called_once()

    @skip("correct it later")
    def test_how_to_ignore(self):
        """
        Shows how to correct it later
        :return:
        """
        pass
