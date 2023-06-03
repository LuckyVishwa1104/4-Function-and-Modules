#6. random module - this module is used to produce random values, this module is used to perform random action such as generating random number and orinting random number.
import random

# choice() - it return randomvalue from given itterable
lst=[2,4,6,8,10,1,3,5,7,9]
print(random.choice(lst))
print(random.choice(lst))
tiple1=("rock",'paper',"scissor")
print(random.choice(tiple1))
print(random.choice("random"))

# randint() - this method is useedd to generate random integer between given range
a=random.randint(1,10)
print(a)
print(random.randint(1,100))
for i in range(10):
    aa=random.randint(1,10)
    print(aa)

# random() - it return a random floating number between 0.1 and 1
print(random.random()) 
print(random.random())

#shuffle() - this method is used to shuffle a sequence
lst2=[2,4,6,8,10,1,3,5,7,9]
print(lst2)
random.shuffle(lst2)
print(lst2)

# uniform - it return the of two specified numbers
ab=random.uniform(5,6)
print(ab)
print(random.uniform(2,3))