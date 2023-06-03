# this is another module of name module_3 and it is importing module_2
import module_2
# if we import any module using import satement, then entire program is get executed, to avoid this therer are other methods of importing discussed in imorting section.
# it is using the fac functoin of module_2
print(module_2.fac(5))
print(module_2.fac(10))

# we can import multiple modules in a single program.
# this is also using the module_1, and inherit the add function of module_1
import module_1
print(module_1.add(200,400))
print(module_1.add(90,302))

# this module is having function greet
def greet(name):
    print(name,"Hello you !!!")
# it also has second function quote
def quote():
    print("Something later, becomes Never. Do it now...")
