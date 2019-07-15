from flask_restplus import fields, Namespace


class DogDTO:
    """ DTO  for all kindts of Dog responses """
    dogs_api = Namespace("dogs", description="Dogs api")

    dogs_parent = dogs_api.model('parent', {
        'parent_name': fields.String,
        'parent_gender': fields.String

    })
    cat_fields = dogs_api.model('dog', {
        'name': fields.String,
        'age': fields.Integer,
        'parent': fields.Nested(dogs_parent)
    })

    dogResponse = dogs_api.model('DogResponse', {
        'description': fields.String,
        'dogs': fields.List(fields.Nested(cat_fields))

    })
