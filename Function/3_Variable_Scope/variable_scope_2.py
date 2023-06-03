# example on global and local variable 1
# a and r is declared in main hence it is global by default
a=56
print(a)
r=88
# defining first function
def f1():
	print(r)
	# using global variable will tell this function that a is a global variable
	global a
	a=44
	# defining second function
	def f2():
		# if we dont use global keyword then it will create a new variable with same idetifier.
		global b
		b=78
		print(b)
	# calling second function
	f2()
	print(a)
# calling first function
f1()
# displaying global variables
print(r) 
print(b)
print(a)