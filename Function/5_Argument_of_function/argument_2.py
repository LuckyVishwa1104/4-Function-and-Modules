# Types of Argument- there are four types of argument.
#1). Required argument: these are necessary argument for function execution, they need to be passed in correct order and number.
# the no. of argument and the no. of values should be exactly equal, if any value is missing then it will throw missing argument error.
'''syntax: def func(arg1,arg2,...):
             -----
           func(val1,val2,...)'''

#example 1
def fun1(a,b):
    print("Addition :")
    c=a+b
    print(c)
# value 55 and 89 are assigned to a and b
fun1(55,89)

# example 2
def fun2(h,j):
    print("name is {}, and age is {}.".format(h,j))
    # Lucky is assigned to h and 20 is assigned to age.
fun2("Lucky",20)

#example 3
i1,j1=5,8
k1=eval(input("Enter number : "))
l1=eval(input("Enter number : "))
def fun3(e,f,g,h):
    i=e*f
    j=g/h
    k=f*g/h
    l=e+f/g*h
    print(i,j,k,l)
# values are passed through variables
fun3(i1,j1,k1,l1)