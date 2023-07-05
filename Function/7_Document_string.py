# Document String: it is similar to comment, it is a multiline string used to provide description of function
# it is not ignored by interpreter, it can be displayed in the program
# doc string can be defined only after function definition
'''Syntax:  def func(args):
                """ -----
                doc_string 
                ------ """ 
                function_body '''

# example 1
def greet(name):
    """this function takes one parameter and returns a greeting message"""
    print(f"Hello you! {name}")
greet("LUCKY")

# example 2
def add(a,b):
    """it add two numbers and display the result
    
    parameters: a (int) - first argument
                b (int) - second argument
                
    result:     c (int) - sum of a and b"""
    c=a+b  # function body
    print(f"{a} + {b} = {c} ")
# function call          
add(10,20) 

# example 3
def sum(n):
    """this function does sum of n numbers and return the sum
    
    parameters: n (int) - sum upto this number
    
    return:     sum (int) - sum of n number """
    if n==0:
        return 0
    else:
        s=n+sum(n-1)
    return s
print(sum(10))
# since the doc string is not ignored, it is displayed by __doc__ attribute
print(sum.__doc__)

# example 4
def fac(m):
    """it accept one argument and return its factorial
    
    parameters: m (int) - argument for fatorial
    
    return:     fac (int) - factorial of m """  
    if m==0:
        return 1
    else:
        factorial= m*fac(m-1)   
    return factorial
print(fac.__doc__)
print(fac(5))

# example 5
def greatest_3(x,y,z):
    """ this function accepts three parameters and displays the greatest among three.
    
    parameter:  x (int) - first argument
                y (int) - second argument
                z (int) - third argument
                
    result:     greatest among three numbers """
    if x>y and x>z:
        print(f"{x} is greater than {y}, {z}.")
    else:
        if y>z:
            print(f"{y} is grater than {x} and {z}")
        else:
            print(f"{z} is grater than {x} and {y}")
print(greatest_3.__doc__)            
greatest_3(22,45,36)