#2. from__import statement: using this we can use only selected variables and functions of particular modules
'''Syntax:  from module_name import function_name/*  # using asterisc we can import all function of module
            function_name(arguments)  '''
# importing a module using import statements, will execute the entire module
# for a program being a module it should contain only functions and variable declaration and not the print statements.

# example 1
# this is a module, containing one function
# functioin to add two arguments
def add(a,b):
    c=a+b
    print(f"{a} + {b} = {c}.")

# rest of the program, this part will also get executed when import this module.
print("import_1 module is ended here!")
print("execution terminated")