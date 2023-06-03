# program to swap three no. using function call.
# defining the function
def swap_3_no():
	# assign three no.
	a=3
	b=5
	c=7
	# display the no. before the swaping
	print('''Numbers before swaping:
a={0}
b={1}
c={2}'''.format(a,b,c))
# performing swap operation
	t=a
	a=b
	b=c
	c=t
	# displaying no. after swaping
	print('''Numbers after swaping:
a={0}
b={1}
c={2}'''.format(a,b,c))
	print("End...")
# calling the function
swap_3_no()
# rest of the code
print("Program terminated.")	 