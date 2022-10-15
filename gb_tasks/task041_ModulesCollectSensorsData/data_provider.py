from random import randint

def get_temperature(sensor = 1):
    return randint(-20, 0) if sensor else randint(0, 20)


def get_pressure(sensor = 1):
    if sensor:
        return randint(720, 750)
    else:
        return randint(720, 750)


def get_wind_speed(sensor = 1):
    if sensor == 1:
        return randint(0, 30)
    else:
        return randint(30, 50)


def data_collection():
    return (get_temperature(), get_pressure(), get_wind_speed())
