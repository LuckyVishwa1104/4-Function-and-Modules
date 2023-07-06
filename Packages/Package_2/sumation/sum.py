# this is a function in sum module which is in sumation subpackage
def sum(a):
    f=0
    for i in range(1,a+1):
        f=f+a
    print(f"Sum of first {a} number is {f}")