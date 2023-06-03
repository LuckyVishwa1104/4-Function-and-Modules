# program to add two no. using nested function.
# first function.
def func1():
	# input two number.
	n1=int(input("Enter 1st no. : "))
	n2=int(input("Enter 2nd no. : "))
	# nested/second function 
	# nested function can access the properties of it's prior function
	def func2():
		# performing sum
		n3=n1+n2
		print(n1,"+",n2,"=",n3)
	# calling second function, it will execute later
	func2()
# calling first function, it will execute first.
func1()