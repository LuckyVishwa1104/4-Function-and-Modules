# this is the fifth module
# it contain some variables and functions
a,b="Lucky","Nikhil"
# a program to display sum of nth number.
def sum(l):
    if l==0:
        return 0
    else:
        s=l+sum(l-1)
    return s
# rest of the program