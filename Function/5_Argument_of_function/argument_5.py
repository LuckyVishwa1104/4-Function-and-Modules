#5). Variable Length argument: these are used when we dont know the no. of argument does the function accept.
# we can pass n no. of argument, arguments are stored in tuple.
''' Syntax: def func(*arg_name):  # * is used to indicate Variable Length argument
                -----
                #arg_name=(arg1,arg2,arg3,...)
                -----
            func(arg1,arg2,arg3,...)  '''

# example 1
def fun1(*args):
    # sum of n no.
    sum=0
    # argument values are stored in args named tuple.
    print(args)
    for i in args:
        sum=sum+i
    # returnig the result
    return sum
print(fun1(1,2,3,4,5,6,7,8,9,10))

# example 2
def fun2(*hat):
    # swap two numbers
    for i in hat:
        a,b=hat
    print("Before Swapping.")
    print("a =",a)
    print("b =",b)
    t=a
    a=b
    b=t
    print("Aftre Swapping.")
    print("a =",a)
    print("b =",b)
# we can any no. of parameter
fun2(44,89)
fun2(34,56)

# example 3
def fun3(*name):
    # factorial program
    fac=1
    for i in name:
        fac=fac*i
    return fac
# values are stored in tuple
print(fun3(1,2,3))
print(fun3(1,2,3,4,5))

# we can use required and variable length argument together, but variable length argument must follow required argument
def fun2(w,x,*arg):
    print(w)
    print(x)
    print(arg)
fun2(23,78,3,4,5,6)