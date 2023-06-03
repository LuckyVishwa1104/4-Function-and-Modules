# Lambda Function: it is a un-named or anonymous functoin.
# it is defined in single line and using lambda keyword.
# Syntax:  lambda arguments : expression

# examples 1
# a lambda function without any argument
a = lambda : print("Hello You !")
# to execute a lambda function we need to call it, to call a lambda function "function_name(arguments)"
a()
# value of lambda function is assigned to variable s
s = lambda : "hello"
print(s())

# example 2
# a lambda function with arguments
add = lambda a,b:a+b
# the argument are passed while calling the lambda function
print(add(5,9))
greet = lambda name : print("Hello,",name,"! how are you.")
greet("Lucky")
greet("Nikhil")

# example 3
# lambda function to print the square of a number
# the expresssion is evaluate and value is assigned to variable sqr
sqr = lambda a : a**2
w=int(input("Enter the number :"))
print("Square of",w,"is",sqr(w))

# example 4
# use of lambda is better shown when they are used as an anonymous function inside another function.
# this function takes the number and return its double value
def fun(n):
    # returns lambda function as a value
    return lambda a:a*n
t=fun(2)
# value is passed as argument to lambda function
print(t(11))

# example 5
# if-else with lambda fnction
# even or odd number
p = lambda x : f"{x} is a Even." if x%2 == 0 else f"{x} is Odd"
print(p(3))
print(p(8))
# gretest among to number
q = lambda l,m : f"{l} is greater than {m}." if l>m else f"{m} is greater than {l}."
print(q(9,5))
print(q(6,9))