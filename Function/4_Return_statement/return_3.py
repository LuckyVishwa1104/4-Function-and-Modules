# return example 3
# sum of n no. using recursive function
# defining the function
def sum(n):
	# termination cindition
	if n==0:
		return 0
	# recursive execution of function
	else:
		sm=n+sum(n-1)
	# returning the sum value
	return sm
print("Sum is :",sum(int(input("Enter number : "))))