# program to swap two no. using function.
# code to swap two numbers is written in function and it is called for execution 

# define the function

def swap():
	# assign two numbers.
	n1=4
	n2=5
	# display the numbers before swaping
	print('''before swaping :
n1 = {0}
n2 = {1}.'''.format(n1,n2))
	
    # perform swaping using temporary variable.
	t=n1
	n1=n2
	n2=t
	# display result after swaping
	print('''after swaping :
n1 = {0}
n2 = {1}.'''.format(n1,n2))
	
# function call
swap()	
# program terminated