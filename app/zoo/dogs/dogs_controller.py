from flask_restplus import Resource

from app.zoo.dogs.dogs_service import DogService
from app.zoo.dto.dog_dto import DogDTO

dogs_api = DogDTO.dogs_api

_dog_service = DogService()
_dog_dto = DogDTO()


@dogs_api.route('/')
class DogController(Resource):

    @dogs_api.marshal_with(_dog_dto.dogResponse, envelope='DogResponse')
    def get(self):
        return _dog_service.get_dogs()
