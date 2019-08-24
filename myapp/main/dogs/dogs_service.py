from myapp.main.model.dog_model import DogParentDO, DogDO


class DogsResponse:
    """ Response DTO for returning the list of cats """

    def __init__(self, desc, cats):
        self.description = desc
        self.dogs = cats

    def __init__(self, ):
        self.description = ''
        self.dogs = []


class DogService:
    """ Service class for managing the cat resources """

    @staticmethod
    def get_dogs():
        """business method to fetch all dogs """
        resp = DogsResponse()
        resp.dogs = DogService.create_dummy_dogs()
        resp.description = 'This is list of cats'

        return resp

    @staticmethod
    def create_dummy_dogs():
        """returns dummy docs """
        dogs = []
        for i in range(3):
            parent = DogParentDO('Dog Parent' + str(i), 'M')
            dog = DogDO('Dog ' + str(i), i, parent)
            dogs.append(dog)
        return dogs
