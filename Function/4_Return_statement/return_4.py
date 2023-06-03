# example of return  statement 4.
# factorial of a no. using recursive function
# enter the no. of factorial
a=int(input("Enter number :"))
# function to calculate fac.
def fac(n):
	# termination point.
	if n==0:
		return 1
	else:
		# recursively caliing the same function 
		result=n*fac(n-1)
	# returning the result
	return result
# display the output.
print(a,"! =",fac(a))