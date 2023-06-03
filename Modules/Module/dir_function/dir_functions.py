# dir() function: it is used to display the function, variables and classes of particular module
# along with the data-members of module it also displays default python attributes associated with that modules.
'''Syntax :  dir(object)
            objects can be tuple, list, set, dictionary and user defined data-objects like variables, function, classes, etc'''

# this module is having functionand variables as data-member
def fun():
    print("Hello You !")
var1=45
var2=55
print(dir())

# importing another module
# using the from_immport statement it displlays function and variables of that module
from module_1 import add
print(dir())

# importing other module
# using import statement it display module as a object
import module_2
print(dir())

# using other object for dir function
variable=23
print(dir())

# using collection data-type
# passing as argument
lst=[2,3,4,5]
tpl=(2,22,222,2222)
print(dir(lst))
print(dir(tpl))