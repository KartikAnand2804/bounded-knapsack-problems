def dynamicknapsack(weight:list, profit:list, cap:int, size:int): 
	dp = [[-1]*(cap+1) for i in range(size+1)]

	# initializing the zeroeth row and zeroeth column
	for i in range(0, size+1):
		dp[i][0] = 0

	for j in range(0, cap+1):
		dp[0][j] = 0

	# filling the dp matrix 
	for i in range(1, size+1):
		for j in range(1, cap+1):
			if weight[i-1] <= cap:
				dp[i][j] = max(profit[i-1] + dp[i-1][j-weight[i-1]], dp[i-1][j])
			else:
				dp[i][j] = dp[i-1][j]

	return dp[size][cap]




if __name__ == '__main__':
	profit = [1, 4, 5, 7]
	weight = [1, 2, 4, 5]
	cap = 7
	size = len(weight)

	print(dynamicknapsack(weight, profit, cap, size))