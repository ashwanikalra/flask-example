from flask_restplus import fields, Namespace


class CatDTO:
    """ DTO  for all kindts of Cat responses """
    cats_api = Namespace("cats", description="cats api")

    cat_create_req = cats_api.model('Cat', {
        'name': fields.String(description='Name of the cat'),
        'age': fields.Integer(description='age of cat'),
        'color': fields.String(description='color of cat'),
        'breed': fields.String(description='breed of cat')

    })
