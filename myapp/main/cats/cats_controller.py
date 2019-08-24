#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Module cotains class for exposing API for cats

"""
from flask import request
from flask_restplus import Resource


from myapp.main.cats.cat_converter import CatConverter
from myapp.main.cats.cats_service import CatService
from myapp.main.dto.cat_dto import CatDTO

cats_api = CatDTO.cats_api

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

    @cats_api.marshal_with(_catDTO.catResponse, envelope='Response')
    def get(self):
        """
        method return the list of cats when get request is given.
        :return: CatResponse json
        """

        return _cat_service.get_cats()

    @cats_api.expect(_catDTO.cat_create_req, validate=True)
    def post(self):
        """
        method handles the post request to create a cat object
        :return: status
        """
        # args = parser.parse_args()
        cat_dto = CatConverter.get_cat(request.json)
        _cat_service.create_cat(cat_dto)

        # todo return the success status with http code


# @cats_api.route('/')
# class CachedCat(Resource):
#     @cats_api.marshal_with(_catDTO.catResponse, envelope='Response')
#     @CatDTO.cats_cached_api.route('cachedcats')
#     # @mycache.cached(key_prefix=get_key(request))
#     def get_cats(self):
#         """
#         method return the list of cats when get request is given.
#         :return: CatResponse json
#         """
#         return _cat_service.get_cats()
