import sys, os

def class_count(state):
	c = 0
	for i in range(size):
		if state[i]:
			c |= 1 << classes[i]
	return c.bit_count()

def weight_count(state):
	return sum([weights[i] for i in range(size) if state[i]])

def valid(state):
	return weight_count(state) <= capacity

def value_of(state):
	v = sum([values[i] for i in range(size) if state[i]])
	return v

def input(path):
  with open(path, "r") as fi:
    capacity = int(fi.readline())
    numClasses = int(fi.readline())

    weights = [int(u) for u in fi.readline().split(", ")]
    values = [int(u) for u in fi.readline().split(", ")]
    classes = [int(u)-1 for u in fi.readline().split(", ")]
    
    size = len(values)

  return size, capacity, numClasses, weights, values, classes

def output(path):
  with open(path, "r") as fi:
    best = int(fi.readline())
    bestWay = [int(u) for u in fi.readline().split(", ")]

  return best, bestWay

if __name__ == '__main__':
  inputPath = sys.argv[1]
  outputPath = sys.argv[2]

  global size, capacity, numClasses, weights, values, classes, best, bestWay

  size, capacity, numClasses, weights, values, classes = input(inputPath)
  best, bestWay = output(outputPath)

  print(f'>> {best} >< {value_of(bestWay)}')
  print(f'>> {capacity} >< {weight_count(bestWay)}')
  print(f'>> {numClasses} >< {class_count(bestWay)}')