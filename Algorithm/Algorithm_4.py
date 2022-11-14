# ALGORITHM 4
# Genetic algorithms

import sys

capacity = 0
numClasses = 0
size = 0

weights = []
values = []
classes = []

best = -1
bestWay = []


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

    fi.close()

    # OUTPUT
    fo = open(outputPath, "w")

    fo.write(str(best) + "\n")
    fo.write(", ".join([str(u) for u in bestWay]))

    fo.close()


if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print('usage:\Algorithm_4.py <input_file> <output_file>')
        sys.exit(0)
    
    main(sys.argv[1], sys.argv[2])