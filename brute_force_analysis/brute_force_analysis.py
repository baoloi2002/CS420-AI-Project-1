# ALGORITHM 1
# Brute force searching

import sys
import os



def updateSolution():
    global best, bestWay
    cap = 0
    val = 0
    lstClass = []

    for i in range(size):
        if f[i]:
            cap += weights[i]
            val += values[i]
            lstClass.append(classes[i])
            
    lstClass = set(lstClass)
    print(cap, val, len(lstClass))
    if cap <= capacity and len(lstClass) == numClasses:
        if val > best:
            best = val
            bestWay = list(f)

def Try(cur):
    global f
    if cur == size:
        updateSolution()
        return

    for i in range(1, -1, -1):
        f[cur] = i
        Try(cur+1)

def solve(_size, _capacity, _numClasses, _weights, _values, _classes):
    global size, capacity, numClasses, weights, values, classes
    size, capacity, numClasses, weights, values, classes = _size, _capacity, _numClasses, _weights, _values, _classes

    global best, bestWay, f
    best, bestWay = -1, []
    f = [0 for _ in range(size)]

    Try(0)

    return best, bestWay