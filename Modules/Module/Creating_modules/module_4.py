# this a module of name module_4, as the file name

# it is importing module_3
import module_3
# we can use every function define in particular module by importing it
# using the greet function of module_3
module_3.greet("~Lucky")
module_3.greet("Nikhil")
# using the quote function of module_3
module_3.quote()

# sum function is defined in this module
def sum(l):
    if l==0:
        return 0
    else:
        s=l+sum(l-1)
    return s

# rest of the program
print("rest of the program .")
