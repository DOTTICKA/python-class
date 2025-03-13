# #Trying to write some python codes
# f = input()
# a = 3+f
# print (a)

# This code takes in a string of any length and prints all character with even index numbers as capital letters.
# My_string = input("Enter your string: ")
# new_codeupper = []
# new_codelower = []
# for i in range(len(My_string.strip()[:])):
#     if i % 2 == 0:
#         new_codeupper.append(My_string[i].strip().upper())
#     else:
#         new_codeupper.append(My_string[i].strip().lower())
# print(new_codeupper)
# print(new_codelower)

# # creating a list
# list1 = ['Apple', 'Banana', 'Cherry']
# print(list1)
# list2 = list1[1:]
# list3= list1[-1]
# print(list2)
# print(list3)
# print(len(list1))

# list4 = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'almond', 'grape', 'guava', 'lime', 'berry']
# # list5 = [1,2,4,5,6,7,8]
# # print(list4[1:9:2])
# # print(list4)
# # print(list4[-1])
# # print(list4[-7:-1])

# # # fruit = input("What is the name of fruit: ")
# # if fruit in list4:
# #     print("yes, apple is in the list")
# # else:
# #     print("fruit is not in the list")
# #     list4.append(fruit)
# print(list4)

# # for fruit in list4:
# #     print(f'like this {fruit}')

# list4[2:4] = ["pineapple", 'watermelon', 'vine']
# print(list4)
# # tuple1 = (3,4,5,6,7)
# # print(tuple1)

# Tuples

# my_tuple = (5, 46, 7)
# print(type(my_tuple))
# print(dir(my_tuple))
# print(my_tuple.__sizeof__())

# tup = ('apple',) # without adding a comma, python will not recognize the item in tup as a tuple.
# print (type(tup))

#tuple is immutable, so to modify a tuple, we first convert it to a list and then convert back to a tuple.

# tup1 = (4, 6, 7, 3)
# print (type(tup1))
# y = list (tup1)
# y[1] = "kiwi"
# tup2 = tuple(y)
# print(tup2)

#unpacking tuples
# fruits = ('apple', 'banana', "raspberry",'cherry', 'strawberry')
# (green, yellow, *red) = fruits #because of the * added to red, 
# #the rest of the values were added to rest and printed as list.
# print(green)
# print(yellow)
# print(red)

# # Sets
# s1 = {'apple', 'banana', 'cherry', True, 1, 2, 0, False}
# print(s1)
# # print(dir(s1))
# # accessing set items is done with the in function.
# s1.add('orange')
# print(s1)
# #adding items to a set
# s2 = ('Gold', 'Bridget', 'orange')
# s1.update(s2)
# print(s1)
# #removing items from a set
# s1.remove("banana")
# print(s1)

#Dictionary

# d1 = {
#     "brand": "Ford", 
#     'model':'Mustang', 
#     'year': 1954
#     }
# print(d1['brand'])

# a = int(input("What is your number?: "))
# b = int(input("Do you have another number?: "))
# if b > a:
#     print("B is greater than A.")  
# elif b < a:
#     print('B is less than A') 
# else:  
#     print('A is equal to B')
#  #tenary statement: this is when we have an if else statement writtern in one line.

#Checking if increment operation is possible on a list.

# list1 = []
# list1.append(input("Enter your words: "))

# i = 1
# while i < 6:
#     print (i, end = '')
#     if (i == 3):
#         break
#     i += 1

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i, end = '')

# fruits = ['apple', "banana", 'cherry']
# for x in fruits:
#     print(f"I love {x}.", end = " ") #this prints all the parts in the print statement in one line.

# fruits = ['apple', "banana", 'cherry']
# # for x in fruits:
# print(fruits[2][1])

# for x in range(1, 7, 2):
'''In the range function, the first num = the start point of the range, the second num = tells the end point
while the third num = the incremental step for the range operation.
'''
    # print(x, end = " ")

# # Nested loop
# adj = ['red', 'big', 'tasty']
# fruits = ['apple', 'banana', 'cherry']
# for x in adj:
#     for y in fruits:
#         # print(x, y, end = " ")
#         print(x, y)
    
# print("#\n" * 4) #or 

# for i in range(4):
#     print("#", end = " ")# because of the end = " " statement the four # will print in one line.

# for i in range(4):
#     print("#"*4)
#     # OR
# for i in range (4):
#     for i in range(4):
#         print("#", end = ' ') # this allows the code to run in the form of a square.
#     print()
''''
We are learnig list Comprehension'
'''
# fruits = ['apple', 'banana', 'cherry', 'kiwi','mango']
# newlist = [x for x in fruits if "a" in x]#this starts with x because it checks each character (the first x),
# # for item (the second X after the for statement) first and proceeds to the if statement.
# print(newlist)
# # #  Condition statements are said to be optional.

# fruits = ['apple', 'banana', 'cherry', 'kiwi','mango']
# for x in fruits:
#     if "a" in x:
#         newlist = x # This allows the individual groups to be printed individually as a list.
#         print(newlist, end = ". ")

# newlist = [x for x in range(10) if x < 5]
# print (newlist)

# newlist = [x for x!=0 in range(10) if x%3== 0 ]
# print (newlist)

# x = 5//3
# print(x)

# list1 = ['banana', 'apple', 'cherry']
# for x in list1:
#     list2 = x.upper()
#     print (list2)

# list1 = ['banana', 'apple', 'cherry']
# newlist = [x.upper() for x in list1 ]
# print(newlist)

# list1 = ['apple', 'banana', 'cherry', 'kiw', 'mango']
# newlist = [x for x in list1 if x != 'cherry']
# print(newlist)

# list1 = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
# newlist = [x if x != "banana" else "orange" for x in list1]
# print(newlist)

''''
sorting items on a list
'''

# list1 = ['apple', 'banana','orange', 'pineapple', 'cherry', 'kiwi', 'mango']
# list1.sort()
# print(list1)

# list1 = ['apple', 'banana','orange', 'pineapple', 'cherry', 'kiwi', 'mango']
# list1.sort(reverse=True)
# print(list1)

'''
Nested Dictionary
This means a dictionary within a dictionary
'''

# family = {'child1' : {'name': "Emil", 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'Child3': {'name': 'linus', 'year': 2011}}
# for x, obj in family.items(): #x represents the keys in the first dictionary, that is: child1 etc
#     print(x)
#     for y in obj: # y represents the items in the main dictionary
#         print(y + ':', obj[y])#
#     print()

'''
FUNCTIONS
in python you can do 1. procedural 2. function 3. object programming in python.
Functions makes your code reuseable and saves time and space in the process of coding.
'''

def fun1(fname):
    print(fname + " Refsnes")

fun1("Emil")

