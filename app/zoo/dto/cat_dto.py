from flask_restplus import fields, Namespace


class CatDTO:
    """ DTO  for all kindts of Cat responses """
    cats_api = Namespace("cats", description="cats api")

    cat_parent = cats_api.model('parent', {
        'parent_name': fields.String,
        'parent_gender': fields.String

    })
    cat = cats_api.model('cat', {
        'name': fields.String(),
        'age': fields.Integer(min=2),
        'parent': fields.Nested(cat_parent)
    })

    catResponse = cats_api.model('CatsResponse', {
        'description': fields.String,
        'cats': fields.List(fields.Nested(cat))

    })

    cat_create_req = cats_api.model('CatRequest', {
        'cat': fields.Nested(cat)

    })
