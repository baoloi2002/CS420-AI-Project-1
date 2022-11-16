# ALGORITHM 3
# Local beam search
import os

MAX_STEP = 100
MAX_SURVIVE = 5

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

def fitness(state):
	c = numClasses - class_count(state)
	w = weight_count(state)
	pen = c**2 * max(values) + w * sum(values) / sum(weights)
	score = value_of(state) - pen
	return score

def get_childs(state):
	childs = []
	for i in range(size):
		if state[i] == 0:
			new_state = state.copy()
			new_state[i] = 1
			if valid(new_state): 
				childs.append(new_state)
	return childs

def test(state):
	global best_value, best_state
	if class_count(state) == numClasses and value_of(state) > best_value:
		best_value = value_of(state)
		best_state = state

def solve(_size, _capacity, _numClasses, _weights, _values, _classes):
	global size, capacity, numClasses, weights, values, classes
	size, capacity, numClasses, weights, values, classes = _size, _capacity, _numClasses, _weights, _values, _classes

	global best_value, best_state
	best_value, best_state = -1, []

	initial_state = [0 for i in range(size)]
	queue = [initial_state]
	for step in range(MAX_STEP):
		print(f'>> local beam step: {step}')
		childs = []
		for state in queue:
			childs.extend(get_childs(state))

		for state in childs: 
			test(state)

		print(f'>> current found: {best_value}')
		
		childs.sort(key=fitness, reverse=True)
		queue = childs[:MAX_SURVIVE]

	return best_value, best_state
