#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Module contains dog related DB model classes.

"""


class DogParentDO:
    """ Dog's Parent Model Object """

    def __init__(self, name, gender):
        self.parent_name = name
        self.parent_gender = gender


class DogDO:
    """ Dog Model object """

    def __init__(self, name, age, parent):
        self.name = name
        self.age = age
        self.parent = parent
