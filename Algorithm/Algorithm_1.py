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


def main(inputPath, outputPath):
    global capacity, numClasses, weights, values, classes, size, f, best, bestWay
    best = -1
    bestWay = []

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
                


    
    print('Usage:\Algorithm_1.py <input_file> <output_file>')
    print('Or')
    print('To run all file:\Algorithm_1.py <input_folder> <output_folder> all')
    sys.exit(0)