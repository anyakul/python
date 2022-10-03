from random import randint

def get_random(min, max, count):
    my_list = []

    for i in range(0, count):
        my_list.append(randint(min, max))
    
    return my_list
