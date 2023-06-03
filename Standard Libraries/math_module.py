#4. math() - this module functions for mathematical and scientific calculations.
import math

# sqrt() - it return the square root of the specified number
print(f"square root of 64 is ",math.sqrt(64))
print(math.sqrt(900))

# pi() - it return the value of pi
print(f"Value of PI is",math.pi)

# factorial() - t return the factorial of specified no.
math.factorial(5)
print(f"8! =",math.factorial(8))

# fabs() - it return the absolute i.e. natural value of specified number
print(math.fabs(-454.0954))
print(math.fabs(math.pi))

# pow(x,y) - it return the yth power of x
print(f"5 raise to 4 is",math.pow(4,5))

# degrees() - it convert he specified randian measure to degrees
a=math.degrees(math.pi/6)
print(f"pi/6 radian is equal to {a} degrees")
print(math.degrees(3.14/3))

# radians() - it convert the specified degrees measure to radians
b=math.radians(60)
print(f"60 degrees is equal to {b} radians")
print(math.radians(30))

# sin() - it return the sine value of specified angle, it accept angle in radians
print(math.sin(math.pi/4))
print(math.sin(math.pi/6))

# cos() - it return the cosine value of specified angle, it accept angle in radians
print(math.cos(math.pi/4))
print(math.cos(math.pi/6))

# tan() - it return the tangent value of specified angle, it accept angle in radians
print(math.tan(math.pi/4))
print(math.tan(math.pi/6))