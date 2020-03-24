#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Module contain service and other supporting classes

"""
from myapp.main.cats.cat_dao import CatDAO


class CatsResponse:
    """ Response wrapper DTO for returning the list of cats """

    def __init__(self, desc, cats):
        self.description = desc
        self.cats = cats
        self.no_of_cats = 0

    def __init__(self, ):
        self.description = ''
        self.cats = []
        self.no_of_cats = 0


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
    def get_cats(age):
        """service method to fetch all cats """
        resp = CatsResponse()
        cats = CatDAO.find_by_age(age)
        resp.cats = cats
        resp.no_of_cats = len(cats)
        resp.description = 'This is list of cats'
        return resp

    @staticmethod
    def get_cached_cats():
        """service method to fetch all cats """
        resp = CatsResponse()

        # resp.cats = CatService._get_dummy_cats()
        resp.description = 'This is list of cats'

        return resp

    @staticmethod
    def create_cat(cat_dict):
        """service method to create cat """
        name = cat_dict.name
