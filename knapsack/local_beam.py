# ALGORITHM 3
# Local beam search

import sys
import os

def test():
    return 5

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
    f = [0 for u in range(size)]

    #solve

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
                

    
    print('Usage:\Algorithm_3.py <input_file> <output_file>')
    print('Or')
    print('To run all file:\Algorithm_3.py <input_folder> <output_folder> all')
    sys.exit(0)