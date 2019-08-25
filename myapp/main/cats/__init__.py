from myapp.main.model.cat_model import CatParentDO, CatDO


def initialize_cats():
    """ private method to initialize cats """
    cats = []
    for i in range(10):
        parent = CatParentDO('Meow Parent' + str(i), 'M')
        cat = CatDO('Meow ' + str(i), i, parent)
        cats.append(cat)
    return cats


# static initialization for cats
myCats = initialize_cats()
