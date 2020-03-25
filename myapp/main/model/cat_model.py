#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Module contains cat related DB model classes.

"""
from myapp.main import db


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
    def find_by_age(age):
        if age:
            cats = db.session.query(CatDO).filter(CatDO.age >= age).all()
        else:
            cats = db.session.query(CatDO).all()

        return cats

    @staticmethod
    def create(cat_dict):
        cat_do = CatDO(cat_dict['name'], cat_dict['age'], cat_dict['color'], cat_dict['breed'])
        db.session.add(cat_do)
        db.session.commit()
        return cat_do
