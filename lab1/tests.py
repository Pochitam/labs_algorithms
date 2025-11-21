import numpy as np
import time
import random
import matplotlib.pyplot as plt
import lab

def generate_dif_chet(size):
    arr1 = np.random.choice(np.arange(0, 2*size, 2), size=size)
    arr2 = np.random.choice(np.arange(1, 2*size, 2), size=size)
    arr1.sort()
    arr2.sort()
    return arr1, arr2

# def generate_ravnomerno_odin(size):
#     arr1 = np.random.randint(0, 2 * size, size=size)
#     arr2 = np.random.choice(np.arange(0, 2 * size), size=size, replace=False)
#     arr1.sort()
#     arr2.sort()
#     return arr1, arr2

def generate_ravnomerno(size):
    arr1 = np.random.uniform(0, 10**5, size)
    arr2 = np.random.uniform(0, 10**5, size)
    arr1.sort()
    arr2.sort()  
    return arr1, arr2

def generate_ravnomer_dif_chet(size):
    arr1 = np.random.choice(np.arange(0, 10**5, 2), size=size)
    arr2 = np.random.choice(np.arange(1, 10**5, 2), size=size)
    arr1.sort()
    arr2.sort()
    return arr1, arr2

def generate_dif_lenght(size):
    arr1 = np.random.uniform(0, 10**5, size)
    arr2 = np.random.uniform(0, 10**5, size//10)
    arr1.sort()
    arr2.sort()  
    return arr1, arr2

def generate_big_value(size):
    arr1 = np.random.uniform(0, 10**10, size)
    arr2 = np.random.uniform(0, 10**10, size)
    arr1.sort()
    arr2.sort()  
    return arr1, arr2

def generate_min_value(size):
    arr1 = np.random.uniform(0, 10**2, size)
    arr2 = np.random.uniform(0, 10**2, size)
    arr1.sort()
    arr2.sort()  
    return arr1, arr2

def generate_same_values(size):
    arr1 = np.full(size, random.randint(0, 900))
    arr2 = np.full(size, random.randint(0, 900))
    arr1.sort()
    arr2.sort()  
    return arr1, arr2

def generate_random(size):
    arr1 = np.random.randint(0, 10**9, size)
    arr2 = np.random.randint(0, 10**9, size)
    arr1.sort()
    arr2.sort()  
    return arr1, arr2