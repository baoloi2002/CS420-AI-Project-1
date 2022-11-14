# ALGORITHM 2
# Branch and bound
# Update the result as soon as it's satisfied
# Prune branches when:
# Current cap > Capacity
# Future value + Current value < Optimal value
# Future number of class + Current number of class < Number of class

import sys

capacity = 0
numClasses = 0
size = 0

weights = []
values = []
classes = []

best = -1
bestWay = []
f = []

# Sum value from i..N
suffixSumVal = []

# Number of class from i..N
suffixNumClass = []


def Try(cur, cap = 0, val = 0, cntClass = 0, lstClass = {}):
    global capacity, numClasses, weights, values, classes, size, f, best, bestWay, suffixSumVal, suffixNumClass
    # Current cap > Capacity
    if cap > capacity:
        return

    # Update the result as soon as it's satisfied
    if cntClass == numClasses and val > best:
        best = val
        bestWay = list(f)
        return
    
    if cur == size:
        return

    # Future value + Current value < Optimal value
    if val + suffixSumVal[cur] < best:
        return

    # Future number of class + Current number of class < Number of class
    if cntClass + suffixNumClass[cur] < numClasses:
        return

    for i in range(2):
        f[cur] = i
        if i:
            if classes[cur] not in lstClass:
                lstClass[classes[cur]] = 0
            if lstClass[classes[cur]] == 0:
                cntClass += 1
            lstClass[classes[cur]] += 1

        Try(cur+1, cap + i*weights[cur], val + i*values[cur], cntClass, lstClass)

        if i:
            if lstClass[classes[cur]] == 1:
                cntClass -= 1
            lstClass[classes[cur]] -= 1
        f[cur] = 0


def pre_calculate():
    global suffixSumVal, suffixNumClass, size, classes, values
    suffixSumVal = [0 for u in range(size)]
    suffixNumClass = [0 for u in range(size)]
    lstClass = []
    for i in range(size-1, -1, -1):
        if i+1 < size:
            suffixNumClass[i] = suffixNumClass[i+1]
            suffixSumVal[i] = suffixSumVal[i+1]
        suffixSumVal[i] += values[i]
        if classes[i] not in lstClass:
            suffixNumClass[i] += 1
            lstClass.append(classes[i])


def main(inputPath, outputPath):
    global capacity, numClasses, weights, values, classes, size, f, best, bestWay

    # INPUT
    fi = open(inputPath, "r")

    capacity = int(fi.readline())
    numClasses = int(fi.readline())

    weights = [int(u) for u in fi.readline().split(", ")]
    values = [int(u) for u in fi.readline().split(", ")]
    classes = [int(u) for u in fi.readline().split(", ")]

    size = len(weights)
    f = [0 for u in range(size)]

    # pre-calculate 
    pre_calculate()

    # SOLVE
    Try(0)

    fi.close()

    # OUTPUT
    fo = open(outputPath, "w")

    fo.write(str(best) + "\n")
    fo.write(", ".join([str(u) for u in bestWay]))

    fo.close()


if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print('usage:\Algorithm_2.py <input_file> <output_file>')
        sys.exit(0)
    
    main(sys.argv[1], sys.argv[2])