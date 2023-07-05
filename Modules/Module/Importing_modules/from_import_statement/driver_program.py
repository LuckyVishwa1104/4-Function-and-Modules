# this is a driver program to import different modules.

# importing the first module
from from_import_1 import add
# using the add functionof above module
add(15,25)
add(-8,8)

# importing the second module
from from_import_2 import msg
# using the msg function of from_port_2 module
msg("Lucky")
msg("Nikhil")
# we cant use sqr_cub function of from_import_2 since it had't been imported
# to use it we need to import it 
from from_import_2 import sqr_cub
sqr_cub(6)
sqr_cub(7)

# importing the third module
# only pat function of import_3
from from_import_3 import pat
pat(0)
# we can also imort every functoin of module by using *
from from_import_3 import *
pat(0)
for_loop()

# we can also import the functions and variables by renaming it
from from_import_4 import var1,var2,fac
#importing every functions and variables of from_import_4
a=var1
b=var2
c=a*b
print(f"{a} * {b} = {c}") 
# using the function
print(fac(5))
print(fac(8))

# immporting modules by renaming them
# we can import modules and functions by renaming it, it can be done by using "as" keyword
# function sum of from_import_5 is renamed as module_5
from from_import_5 import sum as module_5
print(module_5(10))
from from_import_5 import sum as module_6
print(module_6(20))