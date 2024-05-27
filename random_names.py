import random

user = input("Enter names seperated by(,): ")
list = user.split(',')
print(list)
length = len(list)
list1 = random.randint(0,length-1)
print(list1)
print(list[list1])
