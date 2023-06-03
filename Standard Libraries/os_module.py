#3. os module - the os module provide functions for interacting with the operating system.
import os

# getcwd() - it return the address of the current file or currently opened folder
a=os.getcwd()
print("Folders original path: ",a)

# chcwd() - it will change the current folder, and move to one previous folder, it will go out of the folder
os.chdir('../')
print("Folder after changing path :",os.getcwd())

# mkdir() - it is used to create a new directory at specified location
os.mkdir("C:\\Lucky Vishwakarma\\$ Python Programs\\4_Function_&_Modules\\Standard Libraries\\os_module_example")
os.mkdir("C:\\Lucky Vishwakarma\\$ Python Programs\\4_Function_&_Modules\\Standard Libraries\\os_module")

# rmdir() - this function is used to delete a directory at specified location
os.rmdir("C:\\Lucky Vishwakarma\\$ Python Programs\\4_Function_&_Modules\\Standard Libraries\\os_module")

# rename() - this function is used to rename a directpr
os.rename("C:\\Lucky Vishwakarma\\$ Python Programs\\4_Function_&_Modules\\Standard Libraries\\os_module_example","C:\\Lucky Vishwakarma\\$ Python Programs\\4_Function_&_Modules\\Standard Libraries\\os_mod_exa")