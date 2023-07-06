# importing all the modules and packages
import Package_2.heading
import Package_2.aadition.add
import Package_2.subtraction.sub
import Package_2.multipli.mul
import Package_2.division.div
import Package_2.factorial.fac
import Package_2.sumation.sum

# input the two numbers
x = eval(input("Enter first number: "))
y = eval(input("Enter second number : "))

# using the functions defined in the modules
Package_2.heading.title() 
Package_2.aadition.add.add(x,y)
Package_2.subtraction.sub.sub(x,y)
Package_2.multipli.mul.mul(x,y)
Package_2.division.div.div(x,y)
Package_2.factorial.fac.fac(5)
Package_2.sumation.sum.sum(10)
