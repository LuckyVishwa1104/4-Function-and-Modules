#4). Keyword Argument: these are the argument in which, argument are assigned values in calling part, position of argument does not matter.
# each argument used in calling part should have to match with argument name used in function definition part.
''' Syntax:  def func(arg1,arg2,..):  
                -----
            func(arg1=val1,arg2=val2,...)  '''

# example 1
def fun1(n,m):
    print(m)
    # program for star pattern
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
        print("")
# paasing argument is same order
fun1(n=5,m="Star pattern")
# passing the argument in different order
fun1(m="Star pattern",n=5)

# example 2
def fun2(a,b,c,d):
    s=a+b+c+d
    print("{0} + {1} + {2} + {3} = {4}".format(a,b,c,d,s))
fun2(a=2,b=5,c=8,d=6)
# order of argument does not matter
fun2(c=8,a=2,d=6,b=5)

# example 3
def fun3(honour1,honour2,honour3):
    print('''1st position = {}
2nd position {}
3rd position {}'''.format(honour1,honour2,honour3))
# assinging to variables
j,k,l="GOLD","SILVER","BRONZE"
fun3(honour3=l,honour2=k,honour1=j)

# we can use required and keyword argument together, but keyword argument always should have to follow required argument.
def fun(a,c,d,b):
    print(a)
    print(b)    
    print(d)
    print(c)
fun(89,59,d=398,b=222)
 # we cant use default and keyword argument together in single function