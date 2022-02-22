def countsubsetdiff(arr:list, diff: int) -> int:
	mid = int((sum(arr) + diff)/2)
	
	if mid %2 != 0:
		return 0
	else:	
		dp = [[0]*(mid+1) for i in range(len(arr))]

		# init the rows
		for i in range(len(arr)):
			dp[i][0] = 1

		# init the cols
		for j in range(1, mid+1):
			dp[0][j] = 0

		# filling the dp matrix
		for i in range(1, len(arr)):
			for j in range(1, mid+1):
				if arr[i-1] <= mid:
					dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
				else:
					dp[i][j] = dp[i-1][j]

		return dp[len(arr)-1][mid]


if __name__ == '__main__':
	s = [1, 1, 2, 3, 5, 0, 3]
	diff = 1
	print(countsubsetdiff(s, diff))