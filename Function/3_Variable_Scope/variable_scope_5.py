# example of global and local variable 4
# a,b is declared as global
a=20
b=55
c=78
def f1():
	# value of b get updated, but it will exists within the function 
	b=80
	print(b)
	def f2():
		# b is used with global keyword, to tell this function that value of b is that value definer in main bidy
		global b
		b=5
		b=b+10
		print(b)
		# c is declared as global, we have declare value of c either in main body or just below global declaration.
		global c
		c=51
		#value of a from main body
		print(a)
	f2()
	# global value of b, because after function f2() definition no value of b is declared.
	print(b)
f1()
# value of a from main body
print(a)
print(b)
print(c)