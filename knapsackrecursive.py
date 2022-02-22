def recursiveknapsack(weight:list, profit: list, cap: int, size:int):
	if cap == 0 or size == 0:
		return 0
	else:
		if weight[size-1] <= cap:
			return max(profit[size-1]+ recursiveknapsack(weight, profit, cap-weight[size-1], size-1), recursiveknapsack(weight, profit, cap, size-1))
		else:
			return recursiveknapsack(weight, profit, cap, size-1)

if __name__ == '__main__':
	profit = [1, 4, 5, 7]
	weight = [1, 1, 4, 5]
	cap = 7

	# max_profit = 12

	size = len(profit)
	print(recursiveknapsack(weight, profit, cap, size))

