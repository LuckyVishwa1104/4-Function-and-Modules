# this is a third module of name as that of file name i.e. from_import_3
# it contains two functions for displaying star pattern

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

# second function
def for_loop():
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
        print()

# rest of the functions