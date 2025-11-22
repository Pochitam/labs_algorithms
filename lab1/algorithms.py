import random
import time
import numpy as np
import matplotlib.pyplot as plt

def two_pointers(arr1, arr2):
    n, m =  len(arr1), len(arr2)
    p1, p2 = 0, 0   
    while p1<n and p2<m:
        if arr1[p1]==arr2[p2]: return True
        elif arr1[p1] > arr2[p2]: p2+=1
        else: p1+=1
    return False

def bin_search_two_arrs(arr1, arr2):
    if len(arr1)>len(arr2):
        arr1, arr2 = arr2, arr1
    n, m =  len(arr1), len(arr2)
    for el in arr1:
        l, r = 0, m-1
        if bin_search(el, arr2, l, r): return True
    return False

def exp_search(arr1, arr2):
    p = 0
    if len(arr1)>len(arr2):
        arr1, arr2 = arr2, arr1
    n, m =  len(arr1), len(arr2)
    for el in arr1:
        k = 1
        if p>=m: break
        if el==arr2[p]: return True
        elif el<arr2[p]: continue
        else:
            l = p
            while p!=(m-1) and arr2[p]<el:
                k *= 2
                p = min(p+k, m-1)
            r = p
            if bin_search(el, arr2, l, r): return True
            p = l
    return False
        
def bin_search(el, arr, l, r):
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == el:
            return True
        elif arr[mid]>el:
            r = mid-1
        else:
            l = mid+1 
    return False   

def bin_search_insert(el, arr, l, r):
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == el: return mid
        if arr[mid]>el: r = mid-1
        else: l = mid+1
    return l

def center_bin(arr1, l1, r1, arr2, l2, r2):
    if l1>r1 or l2>r2: return False
    if (r1-l1)>(r2-l2): return center_bin(arr2, l2, r2, arr1, l1, r1)
    mid = (l1+r1)//2
    id = bin_search_insert(arr1[mid], arr2, l2, r2)
    if id<=r2 and arr1[mid]==arr2[id]: return True
    return center_bin(arr1, l1, mid-1, arr2, l2, id-1) or center_bin(arr1, mid+1, r1, arr2, id, r2)

def start(a, b):
    return center_bin(a, 0, len(a)-1, b, 0, len(b)-1)


