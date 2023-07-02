#3 - example on global and local variable
# two variable declared as global in main body i.e. a and b

a=57
b=88

def f1():
	# use of global keyward will tell to this function that b is global, 
	global b
	# hence value of b is taken as 88 and get updated accordingly.
	b=b+100
	print(b)
	# from here onwards the value global value of will be 188

	def f2():
		# again a is declared as global.
		global a
		a=1
		a=a+100
		print(a)
		# since a is a global variable, any function can change its value
		a="fghbvf"
		#as value a of a are getting updated it will change accordinly.
		a=0
		# from here onwards the value of a will be 0, as it neither updated in below program
		print(a)

		def f5():
			# here a is a local variable to this function, and it will exist within this function only
			a="how"
			print(a)
		f5()
		# at this moment it will search for local value of a if it encounter any local value within this function or functions outside to this function it will consider that value.
		# if it does not find any local value, it will consider the global value and print it.
		print(a)

	f2()
	# global value of a is 0 only
	# value of is updated 

	# here a is a local variable to this function
	a=698 
	def fu():
		# it will again search for local value of a, as it does not found any such value, hence it will print the global value
		print(a)
	fu()

	print(a)
f1()
# since function has been ended the value of a as 698 is destroyed, but the globle value i.e. 0 is restored.
#hence it will display 0
print(a)
a="wwe"
# again value of a is updated it will display "wwe" and from here the value of a become "wwe" as globle for the entire program, because it is in main body, so if this function ends the program will be ended.
print(a)

def f8():
	# it will search for local value of a but it will not get any such value, hence ti will consider the global value of a, and perform the acoordingly actions
	print(a)
f8()