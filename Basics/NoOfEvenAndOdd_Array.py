def nodd_neven(arr, size):
	nodd=0
	neven=0
	for i in range (size):
		if (arr[i]%2 == 0):
			neven = neven + 1
		else:
			nodd = nodd + 1
	print("Number of even numbers: ", neven)
	print("Number of odd numbers: ", nodd)

arr = [1,3,5,7,9,2,4,6,8,10]
size = len(arr)
nodd_neven(arr, size)
