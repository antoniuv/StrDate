import random
import time
import tracemalloc
x=int(input())
y=int(input())
L1=[random.randint(0,x) for i in range(y)]
'''L=[int(x) for x in input().split()]'''

L2 = L1.copy()
L3 = L1.copy()
L4 = L1.copy()
L5 = L1.copy()
L6 = L1.copy()
L7 = L1.copy()
L8 = L1.copy()

def is_sorted(L):
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True

def InsertionSort(L):
    if len(L) > 10**6 - 1:
        print("Nu poate sorta rapid!")
        return L
    for i in range(1,len(L)):
        j = i-1
        key = L[i]
        while j != -1 and L[j] > key:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = key



def CountSort(L):
    fr = [0]*(max(L)+1)
    for x in L:
        fr[x] += 1
    Lt = []
    for i in range(1, len(fr)):
        while fr[i] != 0:
            Lt.append(i)
            fr[i] -= 1
    return Lt

def merge(Lista, st, mij, dr):
    a = mij - st + 1
    b = dr - mij
    L = [0]*a
    R = [0]*b
    for i in range(a):
        L[i] = Lista[st + i]
    for j in range(b):
        R[j] = Lista[mij + 1 + j]
    i = 0
    j = 0
    k = st
    while i < a and j < b:
        if L[i] < R[j]:
            Lista[k] = L[i]
            i += 1
        else:
            Lista[k] = R[j]
            j += 1
        k += 1
    while i < a:
        Lista[k] = L[i]
        i += 1
        k += 1
    while j < b:
        Lista[k] = R[j]
        j += 1
        k += 1


def mergeSort(Lista, st, dr):
    if st < dr:
        mij = st + (dr - st) // 2
        mergeSort(Lista, st, mij)
        mergeSort(Lista, mij + 1, dr)
        merge(Lista, st, mij, dr)


def RadixSort(L):
    nrmax = max(L)
    bucket = [0] * 10
    cop = [0] * len(L)
    p = 1
    while nrmax // p > 0:
        bucket = [0] * 10
        for i in range(len(L)):
            cifra = (L[i] // p) % 10
            bucket[cifra] += 1
        for i in range(1, 10):
            bucket[i] += bucket[i - 1]
        for i in range(len(L) - 1, -1, -1):
            cifra = (L[i] // p) % 10
            cop[bucket[cifra] - 1] = L[i]
            bucket[cifra] -= 1
        for i in range(len(L)):
            L[i] = cop[i]
        p *= 10


def RadixSort16(L):
    nrmax = max(L)
    bucket = [0] * 16
    cop = [0] * len(L)
    p = 1
    while nrmax // p > 0:
        bucket = [0] * 16
        for i in range(len(L)):
            cifra = (L[i] // p) % 16
            bucket[cifra] += 1
        for i in range(1, 16):
            bucket[i] += bucket[i - 1]
        for i in range(len(L) - 1, -1, -1):
            cifra = (L[i] // p) % 16
            cop[bucket[cifra] - 1] = L[i]
            bucket[cifra] -= 1
        for i in range(len(L)):
            L[i] = cop[i]
        p *= 16


def RadixSort216(L):
    nrmax = max(L)
    bucket = [0] * 2**16
    cop = [0] * len(L)
    p = 1
    while nrmax // p > 0:
        bucket = [0] * 2**16
        for i in range(len(L)):
            cifra = (L[i] // p) % 2**16
            bucket[cifra] += 1
        for i in range(1, 2**16):
            bucket[i] += bucket[i - 1]
        for i in range(len(L) - 1, -1, -1):
            cifra = (L[i] // p) % 2**16
            cop[bucket[cifra] - 1] = L[i]
            bucket[cifra] -= 1
        for i in range(len(L)):
            L[i] = cop[i]
        p *= 2**16

def ShellSort(L):
    n = len(L)
    if len(L) > 10**7-1:
        print("Nu poate sorta rapid!")
        return L
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            tmp = L[i]
            j = i
            while j >= gap and L[j - gap] > tmp:
                L[j] = L[j - gap]
                j -= gap
            L[j] = tmp
        gap //= 2



tracemalloc.start()
start_time=time.time()
InsertionSort(L1)
end_time=time.time()
print(f"InsertionSort elapsed time: {end_time - start_time} seconds")
print(f"Memory used: {tracemalloc.get_traced_memory()}")
print(is_sorted(L1))
tracemalloc.stop()

tracemalloc.start()
start_time=time.time()
L2=CountSort(L2)
end_time=time.time()
print(f"CountSort elapsed time: {end_time - start_time} seconds")
print(f"Memory used: {tracemalloc.get_traced_memory()}")
print(is_sorted(L2))
tracemalloc.stop()

tracemalloc.start()
start_time=time.time()
mergeSort(L3,0,len(L3)-1)
end_time=time.time()
print(f"Mergesort elapsed time: {end_time - start_time} seconds")
print(f"Memory used: {tracemalloc.get_traced_memory()}")
print(is_sorted(L3))
tracemalloc.stop()

tracemalloc.start()
start_time=time.time()
RadixSort(L4)
end_time=time.time()
print(f"Radixsort elapsed time: {end_time - start_time} seconds")
print(f"Memory used: {tracemalloc.get_traced_memory()}")
print(is_sorted(L4))
tracemalloc.stop()

tracemalloc.start()
start_time=time.time()
RadixSort16(L5)
end_time=time.time()
print(f"Radixsort16 elapsed time: {end_time - start_time} seconds")
print(f"Memory used: {tracemalloc.get_traced_memory()}")
print(is_sorted(L5))
tracemalloc.stop()

tracemalloc.start()
start_time=time.time()
RadixSort216(L6)
end_time=time.time()
print(f"Radixsort216 elapsed time: {end_time - start_time} seconds")
print(f"Memory used: {tracemalloc.get_traced_memory()}")
print(is_sorted(L6))
tracemalloc.stop()

tracemalloc.start()
start_time=time.time()
ShellSort(L7)
end_time=time.time()
print(f"ShellSort elapsed time: {end_time - start_time} seconds")
print(f"Memory used: {tracemalloc.get_traced_memory()}")
print(is_sorted(L7))
tracemalloc.stop()

tracemalloc.start()
start_time=time.time()
L8=sorted(L8)
end_time=time.time()
print(f"Native sort elapsed time: {end_time - start_time} seconds")
print(f"Memory used: {tracemalloc.get_traced_memory()}")
print(is_sorted(L8))
tracemalloc.stop()

'''i=0
with open("printare","w") as g:
    for x in L:
        g.write(str(x) + " ")
        if i == 9:
            g.write('\n')
            i=0
        else:
            i+=1
g.close()'''
