# Argument of Function: these are values passed to function, which are used as variable in func body.
# arguments are declared in func defination and values are passed in func calling, corres. value get assigned to corres. argument.

''' Syntax: def func(arg1,arg2,...):
	                   --- func body
	             func(val1,val2,...)  '''

# exampels 1
def func1(arg):
	print(arg)
func1("Lucky")
# "Lucky" value is assign to arg, and it is used in func

# example 2
def func2(n,m):
	print("First no. : ",n)
	print("Second no. : ",m)
	k=n+m
	return k
#value 8 and 7, are assign to n & m
print("Sum is :",func2(8,7))

#example 3
def func3(a,b,c):
	# any data-type can passed as argument
	print([a,b,c])
# assiging to variables 
p=(2,4,6)
q=[3,5,(7,1)]
r={"∆","#","©"}
func3(p,q,r)			             	             