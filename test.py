def two_sum(num, target):
	output_Arr = []
	for i in range(len(num)):
		complement = target - num[i]
		if complement in num[i+1:] :
			output_Arr.append((i , num.index(complement, i+1)))
	print(num)
	print(output_Arr)
two_sum([4,5,6,3,2], 7)
