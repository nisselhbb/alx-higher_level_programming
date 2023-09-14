#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    products = 0
    weights = 0
    for score, weight in my_list:
        products += score * weight
        weights += weight
    if weights == 0:
        return 0
    average = products / weights
    return average
