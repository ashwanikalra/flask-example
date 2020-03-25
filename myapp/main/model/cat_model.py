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

    @property
    def get_json(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.cat_id,
            'name': self.name,
            'age': self.age,
            'color': self.color,
            'breed': self.breed
        }
