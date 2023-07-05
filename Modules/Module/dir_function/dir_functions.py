# dir() function: it is used to display the function, variables and classes of particular module
# along with the data-members of module it also displays default python attributes associated with that modules.
'''Syntax :  dir(object)
            objects can be tuple, list, set, dictionary and user defined data-objects like variables, function, classes, etc'''

# this module is having function and variables as data-member
def fun():
    print("Hello You !")
var1=45
var2=55
print(dir())

# importing another module
# using the from_immport statement it displlays function and variables of that module
from module_1 import add
print(dir())
import module_1
print(dir(module_1))

# importing other module
# using import statement it display module as a object
import module_2
print(dir(module_2)) # for a particular module, if we dont know data members of that module we can use dir function to get all the data members of that module

# using other object for dir function
variable=23
print(dir())

# using collection data-type
# passing as argument
lst=[2,3,4,5]
tpl=(2,22,222,2222)
print(dir(lst)) # it return all the functions and methods related to list
print(dir(tpl)) # it return all the function and methods related to tuple