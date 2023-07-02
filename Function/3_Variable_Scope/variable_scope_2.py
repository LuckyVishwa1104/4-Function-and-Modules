#1 - example on global and local variable

# a and r is declared in main hence they are global by default
a=56
print(a)
r=88

# defining first function
def f1():

	# global value of r will bw considered
	print(r)

	# using global variable will tell this function that a is a global variable
	global a
	a=44
	# from here onwards the global value of a is 55 

	# defining second function
	def f2():

		# if we dont use global keyword then it will create a new variable with same idetifier within this function
		global b
		b=78
		print(b)

	# calling second function
	f2()
	print(a)

# calling first function
f1()

# displaying global variables. at this moment all the global values of variables will bw considered
print(r) 
print(b)
print(a)