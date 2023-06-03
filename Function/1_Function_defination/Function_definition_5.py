# program to display multiplication tables, using function.
# defining a function
def multiplication_table():
	# input the number 
	num=int(input("Enter number : "))
	# using nested for loop
	for i in range(1,num+1):
		for j in range(1,11):
			# multiplication operation
			m=i*j
			# displaying result
			print(i,"×",j,"=",m)
		print("")
	print("Finish...")
# rest of the program...
multiplication_table()
print("end")