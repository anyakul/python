from auto import Auto

cars = [
    Auto(make="Kia", model="Sorrento", year="2003",
         mileage="223000", price="415000", origin_ru="Россия"),
    Auto(make="Hyundai", model="Solaris", year="2015",
         mileage="41000", price="869000", origin_ru="Корея"),
    Auto(make="Volkswagen", model="Passat", year="2012",
         mileage="127000", price="900000", origin_ru="Германия"),
    Auto(make="Lada", model="Priora", year="2011",
         mileage="139000", price="150000", origin_ru="Россия"),
    Auto(make="UAZ", model="Patriot", year="2011",
         mileage="150000", price="345000", origin_ru="Россия")
]


listOfCarNames = []

for i in range(0, len(cars)):
    listOfCarNames.append(cars[i].makeModel(i))
    print(cars[i].__repr__())


print(listOfCarNames)


def sortCars():
    sortedByMileage = []
    cars.sort(key=lambda x: x.mileage)

    for i in range(0, len(cars)):
        sortedByMileage.append(cars[i].makeModelMileage(i))

    return sortedByMileage


print(sortCars())
