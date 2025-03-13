
# Attempt on Question 1: Write a code to print the multiplication table 
# from 2 to 12

"""
num1 = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
num2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
for i in num1:
    for j in num2:
        print(f'{num1}x{num2}= {num1}*{num2}')

num1 = 13
if num1 < 13:
    for i in range(1, 13):
        print(num1 * i)
    num1 += 1
num = 2, 12
while True:
"""
# for j in range(2, 13): #this line sets the range of numbers to be multiplied.
#     print(f'\nMultiplication table for {j}') #This line provides a header.
#     for i in range(1, 13): #this sets the range of num to be multiplied by.
#         print(f'{j} x {i} = {j * i}')# prints the final product.
    
#Attempt on Question 2: Write a code to print the calendar of a particular month of the year by taking in user input. it checks if the month is a digit or a full spelling of the months name.

# import calendar as cal
# year = int(input('Enter the year: '))
# month = input('Enter the month: ').strip().capitalize()
# if month.isdigit():
#     month1 = int(month)# month1 refers to the integer value of the month if the input is digit
#     if month1 <= 12:
#         print(cal.month(year, month1))
# else:
#     if month.isalpha():
#         month2 = list(cal.month).index(month)
#         print(cal.month(year, month2))

# elif month.isalpha():
#     month_name = month.lower().strip()
#     print(cal.month_name(year, month))
# else:
#     print('Invalid input. Please enter a valid month.')

# # Attempts at Question 3. 
# # 3a: prints an hour glass image
# char = "*"
# rows = 6
# for i in range(rows):
#     print(" "*i + char * (2 * (rows -i)-1))
# for i in range(rows - 2, -1, -1):
#     print(" " * i + char * (2 * (rows -i)-1))

# #3b: prints a diamond shape
rows = 10
char = "*"
for i in range (rows):
    print(" "* (rows -i -1) + char * (2 * i + 1))
for i in range (rows - 2, -1, -1):
    print(" "* (rows -i -1) + char * (2 * i + 1))

