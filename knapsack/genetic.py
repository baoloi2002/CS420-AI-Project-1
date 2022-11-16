# ALGORITHM 4
# Genetic algorithms
'''
    penClass = countBit(classMask) / numClasses
    penClass**=2
    penCap = capacity - cap
    penCap /= capacity
    return  (val**2)*penClass + penCap*val + val
'''

import sys
import os
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
    # add 1 for the case this individual is not accept the condition
    classMask = 0
    cap = 0
    val = 0
    for i in range(size):
        if f[i]:
            cap += weights[i]
            val += values[i]
            classMask |= (1<<classes[i])
    penClass = countBit(classMask) / numClasses
    penClass**=2
    penCap = capacity - cap
    penCap /= capacity
    return  (val**2)*penClass + penCap*val + val

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




def geneticAlgorithm(population, cycles, mutation):# mutation between 0..1
    old_individual = [genRandom() for _ in range(population)]
    new_individual = []
    point = calculatePoint(old_individual)
    
    for cycle in range(cycles):
        new_individual = list()
        sum = 0
        tmpPoint = []
        last = 0
        for u, v in point.items():
            sum += v
            tmpPoint.append([u, sum])

        for i in range(population):
            u = old_individual[getRandom(tmpPoint, sum)]
            v = old_individual[getRandom(tmpPoint, sum)]

            newChild = reproduce(u, v)

            if random.random() <= mutation:
                newChild[random.randint(0,size-1)] ^= 1
            
            new_individual.append(newChild)
        old_individual = list(new_individual)
        point = calculatePoint(old_individual)
    
    point = calculatePoint(old_individual)
    point = dict(sorted(point.items(),key= lambda x:x[1], reverse=True))
    for u, v in point.items():
        return old_individual[u]

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

def main(inputPath, outputPath):
    global capacity, numClasses, weights, values, classes, size, best, bestWay
    best = -1
    bestWay = []

    # INPUT
    fi = open(inputPath, "r")

    capacity = int(fi.readline())
    numClasses = int(fi.readline())

    weights = [int(u) for u in fi.readline().split(", ")]
    values = [int(u) for u in fi.readline().split(", ")]
    classes = [int(u)-1 for u in fi.readline().split(", ")]

    size = len(weights)
    

    #solve
    # mutation between 0..1
    updateSolution(geneticAlgorithm(1000, 1000, 0.5))
    
    fi.close()

    # OUTPUT
    fo = open(outputPath, "w")

    fo.write(str(best) + "\n")
    fo.write(", ".join([str(u) for u in bestWay]))

    fo.close()


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
        sys.exit(0)
    if len(sys.argv) == 4:
        if sys.argv[3] == 'all':
            index = 0
            while True:
                input = os.path.join(sys.argv[1], "INPUT_"+str(index)+".txt")
                output = os.path.join(sys.argv[2], "OUTPUT_"+str(index)+".txt")
                if not os.path.exists(input):
                    break
                print(input, output)
                main(input, output)    
                index += 1
            sys.exit(0)
                

    
    print('Usage:\Algorithm_4.py <input_file> <output_file>')
    print('Or')
    print('To run all file:\Algorithm_4.py <input_folder> <output_folder> all')
    sys.exit(0)