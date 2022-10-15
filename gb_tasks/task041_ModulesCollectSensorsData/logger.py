from datetime import datetime as dt

file = 'gb_tasks/task041_ModulesCollectSensorsData/data.cvs'

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(file, 'a') as f:
        f.write('{};temperature;{}\n'.format(time, data))


def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(file, 'a') as f:
        f.write('{};pressure;{}\n'.format(time, data))


def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(file, 'a') as f:
        f.write('{};wind_speed;{}\n'.format(time, data))
