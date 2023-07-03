# Return Statement: it return some value, the returned value is assigned to function name. 
# it is optional, it indicate the end of function.

# Example 1
# function definition
def d():
	a=55
	# it is returning value of a i.e. 55
	return a
# here the d() is acting as variable to which returned value is assigned.
print(d())

# second function
def f2():
	b=66
	c=8
	d=b+c
	return d
# assigning to variable
# f2() is holding the value of d i.e. 74
g=f2()
print(g)

# third function
def f3():
	a,b,c=3,7,9
	# returning multiple values
	return a,b,c
# for mult. value it will return them as a collection of tuple
print(f3())

# by default it return none value
def h():
	return
print(h())

# code after return statement will not be execited since it indicate end of function
def f5(a,b):
	c=a+b
	return c
	print("addition  is performed")
	print("end")
	# this part wont be executed as it is written below the return statement
print(f5(5,8))