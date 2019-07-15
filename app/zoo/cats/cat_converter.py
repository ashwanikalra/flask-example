#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module contains classes and utilities for converting json to dto and dto to model etc

"""
from app.zoo.cats.cats_service import CatDataDTO, CatParentDTO


class CatConverter:
    """
    Class contains conversion methods to convert json to dtos and vice versa
    """

    @staticmethod
    def get_cat(req):
        """
        Converts request json into DTO for use by service layer
        :param req: json text
        :return: CatDataDTO
        """
        cat_name = req['cat']['name']
        cat_age = req['cat']['age']
        cat_parent_name = req['cat']['parent']['parent_name']
        cat_parent_gender = req['cat']['parent']['parent_gender']
        parent = CatParentDTO(cat_parent_name, cat_parent_gender)
        dto = CatDataDTO(cat_name, cat_age, parent)
        return dto
