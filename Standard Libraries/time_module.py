# Python Standard Library: Python's standard library is very extensive offering a wide range of facilities.
# Standard libraries are built in modules which contains standard functionalities.
# The libraries afre built for making programming easy.

# there are around 200 python standard libraies, we can get list using help function
help('modules')

'''some of the commonly used libraries are time, sys, os, math, email, random, string, urllib, re, cgi, socket.'''
# 1. time - this module contain function related to time, it is used to handle the time related task.
import time

# time() - it return the no. of second since epoch passed, i.e. current date in seconds
# epoch is the point at which time starts, it is generally "1 January 1970"
current_time = time.time()
print("Current time is in second since epoch passed:",current_time)

# ctime() - it return time in date format, it takes argument as seconds and return time till mentioned seconds from epoch
# it will calculate time from epoch 
sec1=time.ctime(1671891179.2287345)
print("Current time is till epch is",sec1)
# if no parameter is passed it will return the present time
print("present time is",time.ctime())
sec2=time.ctime(1672511400)
print("New Year is on",sec2)
print("Makar Sankranti is on",time.ctime(1673721000))

# sleep() - it will pause the execution for specified time in seconds
print("Next satement will execute after 10 seconds")
time.sleep(10)
print("Execution continued after 10 seconds")

# localtime() - it takes arguments in seconds and return the time in date format i.e. in struct_time format.
sec4=time.localtime(1672511400)
print("New Year is on",sec4)
# if no argument is passed it will return the present date
print(time.localtime())

# mktime() - it takes one argument in struct_time format and return the given time in seconds
sec6=time.mktime(time.localtime(1673807400))
print("Makar Sankranti is on",sec6,"seconds from epoch")