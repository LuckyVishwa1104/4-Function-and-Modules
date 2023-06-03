# program to print prime no. between specified range using definition.
# defining function
def prime_no():   # function header
    # input the number.
	num=int(input("Enter number : "))
	# using nested for loop 
	# outer for loop
	for i in range(2,num+1):
		# inner for loop
		for j in range(2,i):
	# condition to check no. divisibility
			if i%j==0:
				break
		# else with for loop
		else:
			print(i)
	print("program finished!!")
# rest of program.
print("end...")
print("Terminated...")