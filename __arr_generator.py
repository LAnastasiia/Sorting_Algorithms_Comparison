import random

def random_arr_generator(arr_length):
    arr = [1]
    for i in range(arr_length):
        arr += random.seed()
    print(arr)

random_arr_generator(6)
