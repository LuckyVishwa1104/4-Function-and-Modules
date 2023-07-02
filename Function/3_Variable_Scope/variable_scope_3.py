#2 - example on global and local variable

# r is declared in main body hence it is global by default, the use global keyword is optional in main body.
r=474

def f1():

	# we can declare a variable as global for many times
	# from now value of r is 7777 as a global
	global r
	r=7777
	print(r)
	s=66
	print(s)

	# second function
	def f2():
		a=44
		# r is a new local variable to this function and its value will exist within this function only
		r=666
		print(r)
		print(a)
	f2()

	# global valie of r is taken
	print(r)

f1()

# here it will consider the latesst updated value of r
print(r)