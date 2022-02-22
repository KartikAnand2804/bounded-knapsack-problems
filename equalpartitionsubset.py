def equalsumpartition(nums: list) -> bool:
	if sum(nums) % 2 != 0:
		return False
	else:
		target = int(sum(nums)/2)
		
		# initializing the dp matrix with initial values as dp
		dp = [[False]*(target+1) for i in range(len(nums))]

		# init the rows 
		for i in range(len(nums)):
			dp[i][0] = True

		# init the cols
		for j in range(1, target+1):
			dp[0][j] = False

		# filling the dp matrix
			for i in range(1, len(nums)):
				for j in range(1, target+1):
					if nums[i-1] <= target:
						dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
					else:
						dp[i][j] = dp[i-1][j]

		return dp[len(nums)-1][target]




if __name__ == '__main__':
	s = [2, 10]
	print(equalsumpartition(s))