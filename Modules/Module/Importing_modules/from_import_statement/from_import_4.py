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