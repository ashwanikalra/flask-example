#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Module cotains class for exposing API for cats

"""
from flask import request
from flask_restplus import Resource

from myapp.main.cats.cats_service import CatService
from myapp.main.dto.cat_dto import CatDTO
from myapp.main.util import code_profiler

cats_api = CatDTO.cats_api

# private variables for module
_cat_service = CatService()
_catDTO = CatDTO()


@cats_api.route('/')
class Cat(Resource):
    """
    Controller class for exposing the APIs for cats
    """

    @cats_api.doc("get Cats filtered by age",
                  params={'age': "return the cats whose age >= given age"}
                  )
    @code_profiler
    def get(self):
        """
        method return the list of cats when get request is given.
        :return: CatResponse json
        """
        age = request.args.get("age")
        if age:
            cat_age = int(age)
        else:
            cat_age = -1

        cats = _cat_service.get_cats(cat_age)
        return self._get_cats_response(cats)

    @cats_api.doc('Create new cat')
    @cats_api.expect(_catDTO.cat_create_req, validate=True)
    def post(self):
        """
        method handles the post request to create a cat object
        :return: status
        """
        # args = parser.parse_args()
        cat_dict = request.json
        try:
            cat_do = _cat_service.create_cat(cat_dict)
            return self._get_create_response(cat_do, False)
        except Exception as ex:
            print(ex)
            return self._get_create_response(None, True)

    @staticmethod
    def _get_cats_response(cats):
        """
        creates a response json
        :param cats:
        :return:
        """
        response = dict()
        data = dict()
        message = dict()
        message['type'] = 'info'
        message['text'] = 'Success'
        data['message'] = message
        data['cats'] = cats
        response['response'] = data
        return response

    @staticmethod
    def _get_create_response(cat, is_error=False):
        if is_error:
            resp_dict = dict()
            message = dict()
            data = dict()
            message['type'] = 'error'
            message['text'] = 'Some error occured, please see logs'
            data['message'] = message
            resp_dict['response'] = data
            return resp_dict
        else:
            resp_dict = dict()
            message = dict()
            data = dict()
            message['type'] = 'info'
            message['text'] = 'Success. Cat with name {name} created'.format(name=cat.name)
            data['message'] = message
            resp_dict['response'] = data
            return resp_dict


@cats_api.route('/fetchmany')
class CatFetchMany(Resource):
    """
    Controller class for exposing the APIs for cats
    """

    @cats_api.doc("get Cats filtered by age",
                  params={'age': "return the cats whose age >= given age"}
                  )
    @code_profiler
    def get(self):
        """
        method return the list of cats when get request is given.
        :return: CatResponse json
        """
        age = request.args.get("age")
        if age:
            cat_age = int(age)
        else:
            cat_age = -1

        cats = _cat_service.get_cats_fetchmany(cat_age)
        return cats
