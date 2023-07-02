#4 - example of global and local variable
# a,b,c are declared as global

a=20
b=55
c=78

def f1():
	# the default behaviour of '=' operator is to create a new variable in the function 
	b=80
	# so b=80 is a local variable to this function
	print(b)
	
	def f2():
		# b is used with global keyword, to tell this function that value of b is that value defined in main body
		global b 
		# value of b is being updated
		b=5
		b=b+10
		# from here onwards the global value of b will be 15
		print(b)
		# c is declared as global, we have declare value of c either in main body or just below global declaration.
		global c
		c=51
		#value of a from main body
		print(a)
	f2()

	# global value of b i.e. 15, because after function f2() definition no value of b is declared.
	print(b)
f1()

# value of a from main body
print(a)
print(b)
print(c)