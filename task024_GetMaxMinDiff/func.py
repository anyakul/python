import random

def get_random(min, max, count):
    my_list = []

    for i in range(0, count):
        my_list.append(round(random.uniform(min, max), 2))
    
    return my_list
