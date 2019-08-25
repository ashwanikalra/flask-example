from myapp.main.cats import myCats


class CatDAO:

    @staticmethod
    def find_by_age(age):
        cats = []
        for i in range(len(myCats)):
            if myCats[i].age >= age:
                cats.append(myCats[i])

        return cats
