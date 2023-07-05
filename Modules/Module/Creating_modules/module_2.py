# this is another module of name module_2, it is importing the module_1
import module_1
# using the add functipn of the module_1
print(module_1.add(3,7))
print(module_1.add(90,20))

# rest of the program
aa,dd=20,30
print(f"{aa} * {dd} = {aa*dd} ")

# fac function is defined in this module, it can be in used some other function by importing it.
def fac(a):
    if a==0:
        return 1
    else:
        f=a*fac(a-1)
        return f

# rest of the program       
def mul(a,b):
    print(a**b)
mul(5,2)
print("program module_2 get ended")