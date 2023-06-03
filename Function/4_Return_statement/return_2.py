#return statement Example 2
print("Simple Calculator")
print("")
# for addition operarion
def add(x,y):
	return x+y
# for subtraction operarion
def sub(x,y):
	return x-y
# for multiplition operarion
def mul(x,y):
	return x*y
# for division operarion
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
	print(n,"+",m,"=",add(n,m))
elif ch==2:
	print(n,"-",m,"=",sub(n,m))
elif ch==3:
	print(n,"×",m,"=",mul(n,m))
elif ch==4:
	print(n,"÷",m,"=",div(n,m))
else:
	print("Enter above choice.").