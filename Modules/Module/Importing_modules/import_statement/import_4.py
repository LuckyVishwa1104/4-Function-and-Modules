# this is the fourth module
# it contains some variables and functions

# there are two variables
var1=34
var2=56

# function to produce factorial of a number
def fac(n):
    if n==0:
        return 1
    else:
        f=n*fac(n-1)
    return f

# rest of th program
lst={3,6,9,12,151,18}
tpl=(2,4,6,8,10)
lst=[1,21,31,41,15]
dict={1:"one",2:"two",3:"three"}