#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Module cotains class for exposing API for cats

"""
from flask import request
from flask_restplus import Resource

from myapp.main import mycache
from myapp.main.cats.cats_service import CatService
from myapp.main.dto.cat_dto import CatDTO

cats_api = CatDTO.cats_api
cats_cached_api = CatDTO.cats_cached_api

# private variables for module
_cat_service = CatService()
_catDTO = CatDTO()


def get_key(request):
    return "cats"


@cats_api.route('/')
class Cat(Resource):
    """
    Controller class for exposing the APIs for cats
    """

    @cats_api.doc("get Cats filtered by age",
                  params={'age': "age of the cat to filter by"}
                  )
    @cats_api.marshal_with(_catDTO.catResponse, envelope='Response')
    def get(self):
        """
        method return the list of cats when get request is given.
        :return: CatResponse json
        """
        cat_age = int(request.args.get("age"))
        return _cat_service.get_cats(cat_age)

    @cats_api.doc('Create new cat')
    @cats_api.expect(_catDTO.cat, validate=True)
    def post(self):
        """
        method handles the post request to create a cat object
        :return: status
        """
        # args = parser.parse_args()
        cat_dict = request.json
        _cat_service.create_cat(cat_dict)

        # todo return the success status with http code


@cats_cached_api.route('/')
class CachedCat(Resource):

    @cats_api.marshal_with(_catDTO.catResponse, envelope='Response')
    def get(self):
        """
        method return the list of cats when get request is given.
        :return: CatResponse json
        """
        mycache.get("cats")
        cat_age = request.get("age")

        return _cat_service.get_cats(cat_age)
