#return statement Example 2
print("Simple Calculator")
print("")

# for addition operation
def add(x,y):
	return x+y # here it is returning the evaluation of x+y 

# for subtraction operation
def sub(x,y):
	return x-y

# for multiplition operation
def mul(x,y):
	return x*y

# for division operation
def div(x,y):
	return x/y

# enter the two no. for calculation
n=eval(input("Enter first no. :"))
m=eval(input("Enter second no. :"))
print("")

# selection options
print('''For Addition - 1
For Subtraction - 2
For Multuplication - 3
For Division - 4 ''')
print("")

ch=int(input("Enter your choice : "))
if ch==1:
	print(n,"+",m,"=",add(n,m)) # when ever function is called it will print the value of returning object
elif ch==2:
	print(n,"-",m,"=",sub(n,m))
elif ch==3:
	print(n,"×",m,"=",mul(n,m))
elif ch==4:
	print(n,"÷",m,"=",div(n,m))
else:
	print("Enter above choice.")