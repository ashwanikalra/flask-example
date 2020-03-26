#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Module contains cat related DB model classes.

"""
from myapp.main import db
from myapp.main.util import timeit


class CatDO(db.Model):
    """ Cat Model object """
    __table_args__ = {'schema': 'ccdemo'}
    __tablename__ = 'cats'

    cat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    color = db.Column(db.String(45), nullable=True)
    breed = db.Column(db.String(45), nullable=True)

    def __init__(self, name, age, color, breed):
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed

    @staticmethod
    def _transform_resp(cats):
        """
        return dictionary of cats
        :param cats:
        :return: dict of cats
        """
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
    @timeit
    def find_by_age(age):
        cats = db.session.query(CatDO).filter(CatDO.age >= age).all()
        return CatDO._transform_resp(cats)

    @staticmethod
    @timeit
    def find_by_age_fetchmany(age):
        """
        Uses yield_per to better process large result
        :param age:
        :return:
        """
        result = db.session.query(CatDO).yield_per(1000).filter(CatDO.age >= age)
        return CatDO._transform_resp(result)

    @staticmethod
    def create(cat_dict):
        cat_do = CatDO(cat_dict['name'], cat_dict['age'], cat_dict['color'], cat_dict['breed'])
        db.session.add(cat_do)
        db.session.commit()
        return cat_do

    @staticmethod
    def create_bulk(cat_dict):
        """
        Just to create dummy data in buld for processing huge result set
        :param cat_dict:
        :return:
        """
        cat_list = list()
        for i in range(10000):
            cat_do = CatDO(cat_dict['name'] + str(i), cat_dict['age'] + i, cat_dict['color'] + str(i),
                           cat_dict['breed'] + str(i))
            cat_list.append(cat_do)

        db.session.bulk_save_objects(cat_list)
        db.session.commit()
