# Example on  Variable Scope 1
#Global variable - the variables which are accessible throughout the program are known as global variable
#Local variable - the variable which are declared in function are the local variable to that function.

# any variable declared in main body are global by default.
a=77
b=57
# here a and b are global variable
def fun1():
	# it will take value from above declaration
	print(a)
	c=56 # local variable of this function
	print(c)
	d=c*6 # second local variable
	print(d)
fun1()
print(a)
print(b)

# f is a global but it can be accessible to function defined after f declaration
f=67
def func2():
	d=778 # local variable to this function
	print(d)
	print(f)
	def func3():
		e=890 # local variable of this function
		print(e)
		# still it can access d, since it act's as global for this function.'
		print(d)
		print(f)
	func3()
	# these are global to each and every function present
	print(a,b)
func2() 
print(f)

# global keyword - we can make a local variable of a function to global by using global keyword.
aa=7 # global variable for functions onwards
def func7():
	# telling that aa is global, taje its global value
	# the default behaviour of = operator in function is to create a new variable, it always create a local variable.***
	global aa
	aa=aa+7
	print(aa)
func7()
# using global keyword outer function can also access the global value.
def func9():
	def func10():	
		def func11():
			# ai is declared as global
			global ai
			ai=88
			print(ai)
		func11()
		# value of ai is taken from inner function 
		print(ai)
	func10()
	print(ai)
func9()

# Important points on global and local variable identification

#1). global value of a variable is the latest value assigned to that variable after use of global keyword in that function only.

#2). first preference is given to local variable, while execution if local variable is present it will get printed instead of global variable.

#3). it will search for the local variable, in the function where it is printed and in every outer function to that function. If any local variable found it will print it and if not it will print global value. 

#4). all the variable in the main body are global, only the latest value of global variable is considered as global value of that variable.