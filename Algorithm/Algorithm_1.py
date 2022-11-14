# ALGORITHM 1
# Brute force searching

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


def updateSolution():
    global capacity, numClasses, weights, values, classes, size, f, best, bestWay
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

def Try(cur):
    global f, size
    if cur == size:
        updateSolution()
        return

    for i in range(2):
        f[cur] = i
        Try(cur+1)


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
        print('usage:\Algorithm_1.py <input_file> <output_file>')
        sys.exit(0)
    
    main(sys.argv[1], sys.argv[2])