INF = 1000_000_000_000_000_000

def solve(_size, _capacity, _numClasses, _weights, _values, _classes):
	global size, capacity, numClasses, weights, values, classes
	size, capacity, numClasses, weights, values, classes = _size, _capacity, _numClasses, _weights, _values, _classes

	global best_value, best_state
	best_value, best_state = -1, []
  
	print(f'>> size: {size}, cap: {capacity}')

	idx = [i for i in range(size)]
	idx.sort(key=lambda i: classes[i])

	print(f'>> done sort idx by class')

	dp = [[-INF for i in range(2)] for i in range(capacity+1)]

	print(f'>> start dp')

	for i in range(size):
		print(f'>> {i} of {size}')	
		
		old = dp.copy()
		dp = [[-INF for i in range(2)] for i in range(capacity+1)]

		_i = idx[i]

		for j in range(capacity + 1):
			if i == 0:
				if j == 0: dp[j][0] = 0
				if j == weights[_i]: dp[j][1] = values[_i]
			else:
				if classes[_i] == classes[idx[i-1]]:
					dp[j][0] = old[j][0]
					if j >= weights[_i]: 
						dp[j][1] = max(
							old[j][1],
							old[j-weights[_i]][0] + values[_i],
							old[j-weights[_i]][1] + values[_i])
					else: dp[j][1] = old[j][1]
				else:
					dp[j][0] = old[j][1]
					if j >= weights[_i]:
						dp[j][1] = old[j-weights[_i]][1] + values[_i]

	best_value = -1
	for j in range(capacity + 1):
		best_value = max(best_value, dp[j][1])
	best_state = [0 for i in range(size)]

	return best_value, best_state