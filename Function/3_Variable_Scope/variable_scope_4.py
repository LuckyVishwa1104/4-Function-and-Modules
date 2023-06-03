# example on global and local variable 3
# two variable declared as global in main body.
a=57
b=88
def f1():
	# use of global keyward will tell to this function that b is global, 
	global b
	# hence value of b is taken as 88 and get updated accordingly.
	b=b+100
	print(b)
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
		print(a)
		def f5():
			a="how"
			print(a)
		f5()
		print(a)
	f2()
	# global value of a is 0 only
	# value of is updated 
	a=698
	def fu():
		print(a)
	fu()
	print(a)
f1()
# since function has been ended the value of a as 698 is destroyed, but the globle value i.e. 0 is restored.
#hence it will display 0
print(a)
a="wwe"
# again value of a is updayed it will display "wwe" and from here the value of a become "wwe" as globle for the entire program, because it is in main body, so if this function ends the program will be ended.
print(a)
def f8():
	# still value used is updated i.e. "wwe"
	print(a)
f8()