import numpy as np

def gen(n, a, b):
    return (b-a)*np.random.random(n) + a

def ave(list1):
    return sum(list1) / len(list1)


