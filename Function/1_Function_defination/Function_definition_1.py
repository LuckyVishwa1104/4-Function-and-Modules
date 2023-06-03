#1. Function defination - wrapping several logically related statement in single entity.
# In python, every function is need to be defined, function is defined by "def" keyword.
# Syntax:
'''  def function_name():
   	 statement_1
   	 statement_2
   	 statement_3   >>> function_body
   	 - - - - - 
   	 statement_n  '''

# statements can be anything in python i.e. another program, set of instruction, another function, anything.	  	
# every function is associated with function name
# "def" keyword indicate starting of function.
# (): are neccessory, which indicates statement followed by this are part of function.
# statement are logically related to each other.
# function to display message

# example 1
def message():
	print("Hello World !!!")

# example 2
def function_1():
	print("Python Function $")
	print("End")

# example 3
def message1():
	print("Hello !!")
	print("Wecome to Function section.")
	print("Function is set of instruction...")
	print("Function end here.")
print("Rest of Code.")