# importing modules: to use a particular module we need to import it, importing a module is just fetching the module in current program and using its function and variable
# there are different ways to import the modules.

#1. import statement: using import keyword we can use all the functoins and variables of modules at a time, there is no need to import different functions again and again.
'''Syntax:  import module_name
            module_name.function_name(arguments,...) '''
# import statement is prefered for importing standard modules, since they are only meant for importing purpose
# importing a module using import statement, will execute the entire module
# for a program being a module it should contain only function and variable declaration and not the print statements.

# example 1
# this is a module, containing one function
# functioin to add two arguments
def add(a,b):
    c=a+b
    print(f"{a} + {b} = {c}.")
# rest of the program, this part will also get executed when import this module.
print("import_1 module is ended here!")
print("execution terminated")