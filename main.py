import importlib

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

def output(path, best, bestWay):
  with open(path, "w") as fo:
    fo.write(f'{str(best)}\n')
    fo.write(", ".join([str(u) for u in bestWay]))

def process(inputPath, outputPath, algo):
    print(f'>> process file: {inputPath} {outputPath}')

    # INPUT
    size, capacity, numClasses, weights, values, classes = input(inputPath)
    
    #solve
    knapsack = importlib.import_module(f'knapsack.{algo}')
    best, bestWay = knapsack.solve(size, capacity, numClasses, weights, values, classes)

    # OUTPUT
    output(outputPath, best, bestWay)

def process_dir(inputDir, outputDir, algo):
    index = 0
    while True:
        input = os.path.join(inputDir, f'INPUT_{str(index)}.txt')
        output = os.path.join(outputDir, f'OUTPUT_{str(index)}.txt')
        if not os.path.exists(input): break

        process(input, output, algo)
        index += 1

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Optional app description')
  parser.add_argument('--algo', type=str, help='Algorithm number.')
  parser.add_argument('--dir', action='store_true', help='Use input and output directory. If not, using file.')
  parser.add_argument('input', type=str, help='Input file name or directory')
  parser.add_argument('output', type=str, help='Output file name or directory')

  args = parser.parse_args()
  # print("Argument values:")
  # print(args.algo)
  # print(args.dir)
  # print(args.input)
  # print(args.output)

  if args.dir: 
    process_dir(args.input, args.output, args.algo)
  else:
    process(args.input, args.output, args.algo)