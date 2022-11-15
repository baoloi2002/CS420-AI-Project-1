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


def main(inputPath, outputPath):
    global capacity, numClasses, weights, values, classes, size, f, best, bestWay
    best = -1
    bestWay = []
    f = []

    # INPUT
    fi = open(inputPath, "r")

    capacity = int(fi.readline())
    numClasses = int(fi.readline())

    weights = [int(u) for u in fi.readline().split(", ")]
    values = [int(u) for u in fi.readline().split(", ")]
    classes = [int(u)-1 for u in fi.readline().split(", ")]

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
                

    
    print('Usage:\Algorithm_2.py <input_file> <output_file>')
    print('Or')
    print('To run all file:\Algorithm_2.py <input_folder> <output_folder> all')
    sys.exit(0)