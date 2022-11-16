# ALGORITHM 2
# Branch and bound
# Update the result as soon as it's satisfied
# Prune branches when:
# Current cap > Capacity
# Future value + Current value <= Optimal value
# Future number of class + Current number of class < Number of class
# Use binary state representation class

import sys
import os

debug = False

def Try(cur, cap = 0, val = 0, cntClass = 0):
    global f, best, bestWay
    # Current cap > Capacity
    if cap > capacity:
        return

    # Update the result as soon as it's satisfied
    if cntClass == (1<<numClasses)-1 and val > best:
        best = val
        bestWay = list(f)
    
    if cur == size:
        return

    # Future value + Current value < Optimal value
    if val + suffixSumVal[cur] <= best:
        return

    # Future number of class + Current number of class < Number of class
    if (cntClass|suffixNumClass[cur]) != (1<<numClasses)-1:
        return

    for i in range(1,-1,-1):
        f[cur] = i
        Try(cur+1, cap + i*weights[cur], val + i*values[cur], cntClass|(i*(1<<(classes[cur]))))
        f[cur] = 0


def pre_calculate():
    global suffixSumVal, suffixNumClass, size, classes, values
    suffixSumVal = [0 for u in range(size)]
    suffixNumClass = [0 for u in range(size)]
    
    for i in range(size-1, -1, -1):
        if i+1 < size:
            suffixNumClass[i] = suffixNumClass[i+1]
            suffixSumVal[i] = suffixSumVal[i+1]
        suffixSumVal[i] += values[i]
        suffixNumClass[i] |= 1<<(classes[i])

def solve(_size, _capacity, _numClasses, _weights, _values, _classes):
    global size, capacity, numClasses, weights, values, classes
    size, capacity, numClasses, weights, values, classes = _size, _capacity, _numClasses, _weights, _values, _classes

    global best, bestWay, f
    best, bestWay = -1, []
    f = [0 for _ in range(size)]

    # pre-calculate 
    pre_calculate()

    # SOLVE
    Try(0)

    return best, bestWay