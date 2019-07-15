#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Module cotains class for exposing API for cats

"""
from flask import request
from flask_restplus import Resource

from app.zoo.cats.cat_converter import CatConverter
from app.zoo.cats.cats_service import CatService
from app.zoo.dto.cat_dto import CatDTO

cats_api = CatDTO.cats_api

# private variables for module
_cat_service = CatService()
_catDTO = CatDTO()


@cats_api.route('/')
class CatController(Resource):
    """
    Controller class for exposing the APIs for cats
    """

    @cats_api.marshal_with(_catDTO.catResponse, envelope='CatResponse')
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
