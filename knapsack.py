profit = [1, 4, 5, 7]
weight = [1, 3, 7, 5]
cap = 7

item = list()

# time complexity is nlgn

for i in range(len(profit)):
	item.append([profit[i]/weight[i], profit[i], weight[i]])

print(sorted(item, reverse=True))

max_profit = 0
if len(profit) == 0 or len(weight) == 0:
	print(max_profit)
else:
	for elem in sorted(item, reverse=True):
		if cap != 0 or elem[2] < cap:
			max_profit += elem[1]
			cap -= elem[2]
			print(max_profit)
		else:
			break

print('The final profit is:', max_profit)
