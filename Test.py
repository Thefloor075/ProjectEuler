

sum_m = 0
for i in range(100):
	for j in range(100):
		sum_m = max(sum_m,sum(list(int(element) for element in str(i**j))))
print(sum_m)
