class Auto:
    id = None
    name = None
    order = {}

    def __init__(self, make, model, year, mileage, price, origin_ru):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price
        self.origin_ru = origin_ru

    def makeModel(self, i):
        return f'auto{i}: {self.make} {self.model}'

    def makeModelMileage(self, i):
        return [f'{self.make} {self.model}', f'{self.mileage}']

    def getAttrValue(self, attr):
        return getattr(self, attr)

    def __repr__(self):
        return f'{self.make} {self.model} - Price: RUB{self.price}, Production Year: {self.year}, Mileage: {self.mileage}'
