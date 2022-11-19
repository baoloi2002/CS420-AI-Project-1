# ALGORITHM 4
# Genetic algorithms
"""
    if cap > capacity or classMask != (1<<numClasses)-1:
        return -1
    return val*val/cap
"""

import random
import math

def reproduce(x, y):
    w = random.randint(0, size)
    res = x[:w] + y[w:]
    return res

def genRandom():
    res = [random.randint(0, 1) for _ in range(size)]
    return res

def getRandom(point, sum):
    w = random.random()*sum
    l = 0
    r = len(point)-1
    ans = 0
    while l<=r:
        mid = (l+r)//2
        if point[mid][1] <= w:
            ans = mid
            l = mid+1
        else:
            r = mid-1
    return point[ans][0]

def countBit(u):
    u = int(u)
    cnt = 0
    u = 1
    while u > 0:
        if u&1:
            cnt += 1
        u >>= 1
    return cnt


def calculate(f):
    classMask = 0
    cap = 0
    val = 0
    for i in range(size):
        if f[i]:
            cap += weights[i]
            val += values[i]
            classMask |= (1<<classes[i])
    if cap > capacity or classMask != (1<<numClasses)-1:
        return -1
    return val*val/cap

def calculatePoint(f):
    # stable softmax ?
    point = {}
    for i in range(len(f)):
        point[i] = calculate(f[i])
    mx = point[0]
    sum = 0
    for i in range(len(f)):
        mx = max(mx, point[i])
    for i in range(len(f)):
        point[i] = math.exp(point[i]-mx)
        sum += point[i]
    for i in range(len(f)):
        point[i] /= sum

    return point


def updateSolution(f):
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
    
    if cap <= capacity and len(lstClass) == numClasses:
        if val > best:
            best = val
            bestWay = list(f)

def upSols(lstSol):
    for u in lstSol:
        updateSolution(u)


def geneticAlgorithm(population, cycles, mutation):# mutation between 0..1
    old_individual = [genRandom() for _ in range(population)]
    new_individual = []
    point = calculatePoint(old_individual)
    upSols(old_individual)
    
    for cycle in range(cycles):
        new_individual = list()
        sum = 0
        tmpPoint = []
        for u, v in point.items():
            sum += v
            tmpPoint.append([u, sum])

        for i in range(population):
            u = old_individual[getRandom(tmpPoint, sum)]
            v = old_individual[getRandom(tmpPoint, sum)]

            newChild = reproduce(u, v)

            for j in range(size):
                if random.random() <= mutation:
                    newChild[j] ^= 1
            
            new_individual.append(newChild)
        old_individual = list(new_individual)
        upSols(old_individual)
        point = calculatePoint(old_individual)


def solve(_size, _capacity, _numClasses, _weights, _values, _classes):
    global size, capacity, numClasses, weights, values, classes
    size, capacity, numClasses, weights, values, classes = _size, _capacity, _numClasses, _weights, _values, _classes

    global best, bestWay, f
    best, bestWay = -1, []
    f = [0 for _ in range(size)]

    #solve
    # mutation between 0..1
    geneticAlgorithm(500, 500, 0.001)

    return best, bestWay