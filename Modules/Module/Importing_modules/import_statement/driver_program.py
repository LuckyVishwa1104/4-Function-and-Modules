# this is a driver program to import different modules.

# importing 1st module and its function
import import_1
# using add functoin of import_1
import_1.add(12,18)
import_1.add(30,60)

# importing second module and its functioins
import import_2
# accessing the square and cube function
import_2.sqr_cub(9)
import_2.sqr_cub(7)
# using the greet functioin
import_2.msg("Lucky")
import_2.msg("NIkhil")

# importing third module and its functions
import import_3
# using the ascending star pattern of module import_3
import_3.pat(0)

# import fourth module and its function and variables
import import_4
# using the variables of module
aa=import_4.var1
bb=import_4.var2
cc=aa+bb
print(f"{aa} + {bb} = {cc} ")
# using the function
print(import_4.fac(5))

# importing the renamed modules:
# we can import modules and functions by renaming it, it can be done by using "as" keyword
import import_5 as module_5
# module import_5 is renamed as module_5
v1=module_5.a
v2=module_5.b
print(f"variable of module5 are {v1} and {v2}")
# we can rename a single module as many times 
import import_5 as new_module
print(new_module.sum(10))
print(new_module.a)
print(new_module.b)
import import_5 as new_module_2
print(new_module_2.sum(20))