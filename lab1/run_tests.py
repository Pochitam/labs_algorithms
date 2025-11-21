import numpy as np
import time
import matplotlib.pyplot as plt
import lab
import tests

def measure_time(func, arr1, arr2):
    start_time = time.time()
    func(arr1, arr2)
    return time.time() - start_time

def value_times(func):
    for size in sizes:
        arr1, arr2 = func(size)
        
        times_two_pointers.append(measure_time(lab.two_pointers, arr1, arr2))
        times_bin_search_two_arrs.append(measure_time(lab.bin_search_two_arrs, arr1, arr2))
        times_exp_serch.append(measure_time(lab.exp_search, arr1, arr2))
        times_center_bin.append(measure_time(lab.start, arr1, arr2))
    return times_two_pointers, times_bin_search_two_arrs, times_exp_serch, times_bin_search_two_arrs

def generate_graph(t1, t2, t3, t4):
    plt.plot(sizes, times_two_pointers, label="Два указателя", marker='o', markersize=1)
    plt.plot(sizes, times_bin_search_two_arrs, label="Бинарный поиск", marker='x', markersize=1)
    plt.plot(sizes, times_exp_serch, label="Экспоненциальный поиск", marker='^', markersize=1)
    plt.plot(sizes, times_center_bin, label="Бинарный поиск с разделением", marker='s', markersize=1)
    plt.xscale('log')
    plt.xlabel('Размер массива')
    plt.ylabel('Время выполнения')
    plt.title('График времени от размера')
    plt.legend()
    plt.tight_layout()
    plt.show()

sizes = [x for x in range(10, 10**5, 1000)]
times_two_pointers = []
times_bin_search_two_arrs = []
times_exp_serch = []
times_center_bin = [] 

t1, t2, t3, t4 = value_times(tests.func) # <- сюда название функции
generate_graph(t1, t2, t3, t4)
