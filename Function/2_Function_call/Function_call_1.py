#2. Function calling - it is a statement that invokes the function.
# after defining functuon it does not get executed unless it is called.
# after calling function the control goes to function definition, after execution of function it return back to calling instruction.
# every function is called after the function definition
# Syntax:  function_name()
# examples to call functions
# example 1
def mesg():  # fuction definition
	print("Hello World !")
mesg()    # function call :- function will get executed 
print("")
# example 2
def quote():  
	print(" 'Weak people look themself in mirror, to know how they look..        Strong people look themselve in eyes of others to reflect their personality.'")
	print("")
quote() 
# example 3
def message():
	a=3
	b=6
	print(a,"+",b,"=",a+b)
	# rest of program.
message()
print("Program Terminated !")