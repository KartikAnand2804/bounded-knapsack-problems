def targetsum(nums:list, target:int) -> int:
	mid = int((sum(nums)+target))

	if sum(nums)<abs(target) or mid % 2 != 0:
		return 0 
	else:
		mid = int(mid/2)
		dp = [[0]*(mid+1) for i in range(len(nums))]

		# init the rows
		for i in range(len(nums)):
			dp[i][0] = 1

		# init the cols
		for j in range(1, mid+1):
			dp[0][j] = 0

		# filling the dp matrix
		for i in range(1, len(nums)):
			for j in range(mid+1):
				if nums[i-1] <= mid:
					dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
				else:
					dp[i][j] = dp[i-1][j]

		return dp[len(nums)-1][mid]


if __name__ == '__main__':
	nums = [1, 1, 1, 1, 1]
	target = 3
	print(targetsum(nums, target))