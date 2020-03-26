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
        return cats

    @staticmethod
    def get_cats_fetchmany(age):
        cats = CatDO.find_by_age_fetchmany(age)
        return cats

    @staticmethod
    def create_cat(cat_dict):
        return CatDO.create(cat_dict)
        # CatDO.create_bulk(cat_dict)
