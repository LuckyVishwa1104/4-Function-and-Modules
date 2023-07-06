# this is a function in fac module which is in factorial subpackage
def fac(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    print(f"{a}! = {f}")