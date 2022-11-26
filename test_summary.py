
import argparse, os, sys

def input(path):
    with open(path, "r") as fi:
        capacity = int(fi.readline())
        numClasses = int(fi.readline())

        weights = [int(u) for u in fi.readline().split(", ")]
        values = [int(u) for u in fi.readline().split(", ")]
        classes = [int(u)-1 for u in fi.readline().split(", ")]

        size = len(values)

    return size, capacity, numClasses, weights, values, classes


def process(inputPath):

    # INPUT
    size, capacity, numClasses, weights, values, classes = input(inputPath)

    print(f"[{inputPath}] >> size: {size}, cap: {capacity}, class: {numClasses}, sum val: {sum(values)}, sum weight: {sum(weights)}")


def process_dir(inputDir):
    index = 0
    while True:
        input = os.path.join(inputDir, f'INPUT_{str(index)}.txt')
        if not os.path.exists(input): break

        process(input)
        index += 1
        

if __name__ == '__main__':
    process_dir("test\input")