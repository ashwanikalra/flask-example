#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Module contain service and other supporting classes

"""

from myapp.main.model.cat_model import CatDO, CatParentDO


class CatsResponse:
    """ Response wrapper DTO for returning the list of cats """

    def __init__(self, desc, cats):
        self.description = desc
        self.cats = cats

    def __init__(self, ):
        self.description = ''
        self.cats = []


class CatDataDTO:
    """ DTO containing data about single cat object """

    def __init__(self, name, age, parent):
        self.name = name
        self.age = age
        self.parent: CatParentDTO = parent


class CatParentDTO:
    """ DTO to store the details of parent cat """

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class CatService:
    """ Service class for managing the cat resources """

    @staticmethod
    def get_cats():
        """service method to fetch all cats """
        resp = CatsResponse()

        resp.cats = CatService._create_dummy_cats()

        resp.description = 'This is list of cats'

        return resp

    @staticmethod
    def get_cached_cats():
        """service method to fetch all cats """
        resp = CatsResponse()

        resp.cats = CatService._create_dummy_cats()
        resp.description = 'This is list of cats'

        return resp

    @staticmethod
    def create_cat(cat_dto):
        """service method to create cat """
        name = cat_dto.name

    @staticmethod
    def _create_dummy_cats():
        """ private method to returns dummy cats """
        cats = []
        for i in range(3):
            parent = CatParentDO('Meow Parent' + str(i), 'M')
            cat = CatDO('Meow ' + str(i), i, parent)
            cats.append(cat)
        return cats
