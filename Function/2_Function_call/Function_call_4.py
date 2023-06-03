# program to print patter using functuon call.
# defining the function
def unique_pattern():
	# using first nested loop
	for i in range(1,12):
		for j in range(0,i):
			print("*",end=".")
		print("")
	# using second nested loop
	i=1
	while (i<=10):
		j=10
		while(j>=i):
			print("*",end=".")
			j=j-1
		print("")
		i=i+1
# calling function	
unique_pattern()
# rest of code
print("End...")
print("Terminated...")