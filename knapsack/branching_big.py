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
import time
sys.setrecursionlimit(10000)

debug = False

def getWeight(i, j):
    res = suffixWeight[i]
    j+=1
    if j < size:
        res -= suffixWeight[j]
    return res

def getValue(i, j):
    res = suffixSumVal[i]
    j+=1
    if j < size:
        res -= suffixSumVal[j]
    return res

def future(cur, w):
    res = 0
    l = cur 
    r = size-1
    ans = -1
    while l <= r:
        mid = (l+r)//2
        if getWeight(cur, mid) <= w:
            ans = mid
            l = mid+1
        else:
            r = mid-1
    if ans == -1:
        ans = cur
    else:
        w -= getWeight(cur, ans)
        res += getValue(cur, ans)
        ans += 1
        
    if ans<size and w > 0:
        res += values[ind[ans]]/weights[ind[ans]]*w
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
        #print(best)
    
    if cur == size:
        return

    # Future value + Current value <= current Optimal value
    # Method 1
    if val + suffixSumVal[cur] <= best:
        return
    # Method 2
    if val + values[ind[cur]]/weights[ind[cur]]*(capacity-cap) <= best:
        return
    # Method 3
    if future(cur, capacity-cap) + val <= best:
        return

    # Future number of class + Current number of class < Number of class
    if (cntClass|suffixNumClass[cur]) != (1<<numClasses)-1:
        return

    for i in range(1,-1,-1):
        f[ind[cur]] = i
        Try(cur+1, cap + i*weights[ind[cur]], val + i*values[ind[cur]], cntClass|(i*(1<<(classes[ind[cur]]))))
        f[ind[cur]] = 0


def pre_calculate():
    global suffixSumVal, suffixNumClass, size, classes, values, suffixWeight
    suffixSumVal = [0 for u in range(size)]
    suffixNumClass = [0 for u in range(size)]
    suffixWeight = [0 for u in range(size)]
    
    for i in range(size-1, -1, -1):
        if i+1 < size:
            suffixNumClass[i] = suffixNumClass[i+1]
            suffixSumVal[i] = suffixSumVal[i+1]
            suffixWeight[i] = suffixWeight[i+1]
        suffixSumVal[i] += values[ind[i]]
        suffixWeight[i] += weights[ind[i]]
        suffixNumClass[i] |= 1<<(classes[ind[i]])

def solve(_size, _capacity, _numClasses, _weights, _values, _classes):
    global size, capacity, numClasses, weights, values, classes, ind
    size, capacity, numClasses, weights, values, classes = _size, _capacity, _numClasses, _weights, _values, _classes

    global best, bestWay, f

    start_time = time.time()

    best, bestWay = -1, []
    f = [0 for _ in range(size)]
    ind = [u for u in range(size)]
    ind.sort(reverse=True, key=lambda x: values[x]/weights[x])

    # pre-calculate 
    pre_calculate()

    # SOLVE
    Try(0)

    print("--- %s seconds ---" % (time.time() - start_time))
    
    return best, bestWay