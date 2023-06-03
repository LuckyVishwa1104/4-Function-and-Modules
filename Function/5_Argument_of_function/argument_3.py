#2). Default argument - these are the argument assigned at function definition, if any argument value is missing then the default value is taken by defafult.
'''Syntax:  def func(arg1=val1,arg2=val2,arg3,arg4,...):
                ---- # function body
            func(val3,val4,...)'''

#example 1
def fun1(a=55,b=99):
    # default value are taken, a=55 and b=99 by default
    c=a+b
    print(a,"+",b,"=",c)
fun1() # noargument passed
fun1(44,77) # a is assigned 44 and b is 77 
fun1(30) # first argument value is updated

# example 2
# two different type of argument cant be used at same time, function accepts onlt onr type of argument
def fun2(p=10,r=9):
    print((p*2,r*2))
    print(bool(p),bool(r))
fun2()
# assignig to variables
a,b=14,20
fun2(a,b)
fun2(12) # we can't update second argument by keeping first argument as default

# example 3
def fun3(p=3,q=4,r=5):
    print("Hello you ")
    # before passing arguments values are 3,4,5
    # before passing arguments values are 6,8,10
    print("p =",p,"q =",q,"r =",r) 
fun3()
fun3(6,8,10)

# we can use required and default argument together, but default argument argument must follow required argument.
def fun4(a,b,c=56,d=50):
    print(a)
    print(b)
    print(c)
    print(d)
fun4(67,90,888)
# we can use default with variable length argument.
def f(s=90,*ss):
    print(ss)
    print(s)
f(2,3,4,5,6,7)