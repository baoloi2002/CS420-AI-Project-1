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
sys.setrecursionlimit(2000)

debug = False

def isOk(cur, w):
    d = []
    for i in range(cur, size):
        d.append([values[ind[i]]/weights[ind[i]], weights[ind[i]]])
    d.sort(reverse=True, key = lambda x: x[0])
    res = 0
    i = 0
    while w>0 and i < len(d):
        res += d[i][0]*d[i][1]
        w -= d[i][1]
        i += 1
    return res

def Try(cur, cap = 0, val = 0, cntClass = 0):
    global f, best, bestWay
    # Current cap > Capacity
    if cap > capacity:
        return

    # Update the result as soon as it's satisfied
    if cntClass == (1<<numClasses)-1 and val > best:
        best = val
        bestWay = list(f)
        print(best)
    
    if cur == size:
        return

    if isOk(cur, capacity-cap) + val <= best:
        return

    # Future value + Current value < Optimal value
    if val + suffixSumVal[cur] <= best:
        return
    # Future value + Current value < Optimal value
    if val + suffixRate[cur]*(capacity-cap) <= best:
        return

    # Future number of class + Current number of class < Number of class
    if (cntClass|suffixNumClass[cur]) != (1<<numClasses)-1:
        return

    for i in range(1,-1,-1):
        f[cur] = i
        Try(cur+1, cap + i*weights[ind[cur]], val + i*values[ind[cur]], cntClass|(i*(1<<(classes[ind[cur]]))))
        f[cur] = 0


def pre_calculate():
    global suffixSumVal, suffixNumClass, size, classes, values, suffixRate
    suffixSumVal = [0 for u in range(size)]
    suffixNumClass = [0 for u in range(size)]
    suffixRate = [0 for u in range(size)]
    
    for i in range(size-1, -1, -1):
        if i+1 < size:
            suffixNumClass[i] = suffixNumClass[i+1]
            suffixSumVal[i] = suffixSumVal[i+1]
            suffixRate[i] = suffixRate[i+1]
        suffixRate[i] = max(suffixRate[i], values[ind[i]]/weights[ind[i]])
        suffixSumVal[i] += values[ind[i]]
        suffixNumClass[i] |= 1<<(classes[ind[i]])

def solve(_size, _capacity, _numClasses, _weights, _values, _classes):
    global size, capacity, numClasses, weights, values, classes, ind
    size, capacity, numClasses, weights, values, classes = _size, _capacity, _numClasses, _weights, _values, _classes

    global best, bestWay, f
    best, bestWay = -1, []
    f = [0 for _ in range(size)]
    ind = [u for u in range(size)]
    ind.sort(reverse=True, key=lambda x: values[x]/weights[x])

    # pre-calculate 
    pre_calculate()

    # SOLVE
    Try(0)

    return best, bestWay