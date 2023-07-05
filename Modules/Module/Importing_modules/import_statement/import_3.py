# this is a third module of name as that of file name
# it contains function for displaying star pattern

# functioin 1st, to display star pattern in asscending order using recursive function
n=int(input("Enter no. :"))
# using recursive function
def pat(a):
    b=a
    if a>n:
        return 0
    else:
        def pattern(b):
            if b==0:
                return 0
            else:
                print("*",end="")
            pattern(b-1)
        pattern(b)
        print("")
    pat(a+1)  
