def subsetsum(nums:list, sums:int) -> bool:
	
	# creating the dp matrix with initially false value
	dp = [[False]*(sums+1) for i in range(len(nums))]

	# initialzing the zeroth column in the dp matrix
	for i in range(len(nums)):
		dp[i][0] = True

	# initializing the zeroth row in the dp matrix
	for j in range(1, sums):
		dp[0][j] = False

	# filling the dp matrx
	for i in range(1, len(nums)):
		for j in range(1, sums+1):
			if nums[i-1] <= sums:
				dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
			else:
				dp[i][j] = dp[i-1][j]


	return dp[len(nums)-1][sums]

# debug function to print the dp matrix
def debug(matrix:list):
	for elem in matrix:
		print(elem)


if __name__ == '__main__':
	s = [2, 3, 7, 8, 10]
	target = 1
	print(subsetsum(s, target))