# Return example 5

# program to return area of circle
# input the radius of circle
r=int(input("Enter radius :"))

# function to calculate the area
def area(a):

    area=a*a*(3.14)
    # returning the value of area
    return area

# displaying the results
print("Area of circle with radius",r,"is",area(r))
