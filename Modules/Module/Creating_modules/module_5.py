# this is another module named same as the file name as module_5

# it is importing module_4
import module_4
print(module_4.sum(10))
print(module_4.sum(50))

def msg():
    print("heool")

# we can import the modules defined in same folders only.
# importing thr modules defined in some other folder will raise the module not found error.

# impoting modul3
import module_3
module_3.greet("Arthor Fleck")
module_3.quote()

# importing module2
import module_2
print(module_2.fac(7))

# importing module 1
import module_1
print(module_1.add(900,1200))
