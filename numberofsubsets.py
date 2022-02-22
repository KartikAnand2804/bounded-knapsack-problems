def countsubsets(nums:list, target:int) -> int:
	dp = [[0]*(target+1) for i in range(len(nums))]

	# init the rows
	for i in range(len(nums)):
		dp[i][0] = 1

	# init the cols
	for j in range(1, target+1):
		dp[0][j] = 0

	# filling the dp matrix
	for i in range(1, len(nums)):
		for j in range(1, target+1):
			if nums[i-1] <= target:
				dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
			else:
				dp[i][j] = dp[i-1][j]

	return dp[len(nums)-1][target]




if __name__ == '__main__':
	s = [1, 5, 11, 5]
	target = 11
	print(countsubsets(s, target))