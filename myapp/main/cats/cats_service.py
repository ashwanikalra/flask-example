#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Module contain service and other supporting classes

"""
from myapp.main.model.cat_model import CatDO


class CatService:
    """ Service class for managing the cat resources """

    @staticmethod
    def get_cats(age):
        """
        service method to fetch cats
        :param age:
        :return: list of cats meeting criteria
        """
        cats = CatDO.find_by_age(age)

        cats_list = list()
        for cat in cats:
            cat_dict = dict()
            cat_dict['id'] = cat.cat_id
            cat_dict['name'] = cat.name
            cat_dict['age'] = cat.age
            cat_dict['color'] = cat.color
            cat_dict['breed'] = cat.breed
            cats_list.append(cat_dict)

        return cats_list

    @staticmethod
    def create_cat(cat_dict):
        return CatDO.create(cat_dict)
