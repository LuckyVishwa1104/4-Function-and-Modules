# Python Modules: basically module are python files consisting of different functions and variables
# Every file with .py extension is a module, functions defined in modules can be used in other programs by importing the mpdule in which they are defined.
# Module contains variables, function, classes, etc. Name of the python file is assigned as the module name 

#1. Creating modules: we can create our own modules by just writting the program and functions in it and save it.
# to use that module, simply just import it, by using the file name.
# module_1 is the current file and its name is assigned as module name, add function is defined in this module.
def add(a,b):  
    c=a+b
    return c

# this is the seocnd function assigned in the module
def sub(a,b):
    return a-b

# this is the third function assigned in it
def mul(a,b):
    return a*b

# there can also be some variables in mpdule that can be used in some other module
a=345
b='LGMMERML'
c=4095