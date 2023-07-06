#2. sys - it provides various functions and variables that are used to manipulate different parts of python run-time environment.
# it generally deal with system operations/information i.e. system related to python not the operaring system.
import sys

# version - it return the version of pyhton interpreter
print(sys.version)
print(sys.executable)
print(sys.platform)

# stdin - it is a standard input function
a=sys.stdin.readline()
print(a)

# stdout - it is a standard output function
sys.stdout.write("Output through stdout")
sys.stdout.write("\nthe new way to print a statement")

# exit()- it will stop the execution of function at specified line
print()
print("This will get executed")
print("This will also get execute")
sys.exit()
print("This will not get executed")
# this is not correct but still the program will executed uptil exit
print("this will also")