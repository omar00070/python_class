# make a program to input a salary and print the tax
# - if the salary is or more than 2000 : tax is 25%
# - anything else: tax is 15%

# salary = input("input your salary mr user ")
# salary = int(salary)
# if salary >= 2000:
#     tax = 0.25 * salary
# else:
#     tax = 0.15 * salary
# print("your tax is ",tax)    

# first question:
# Take values of length and width of a rectangle from 
# user and check if it is square or not

# length = int(input("please provide a length "))
# width = int(input("please provide a width "))

# if length == width:
#     print("this is a square")
# else:
#     print("this is not a square")



# second question:
# Take two int values from user and print greatest among them.

#third question:
# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

# fourth question:
# Take input of age of 3 people by user and determine oldest 
# and youngest among them and which one is in between.

# ----first solution -------
age1 = input("first age")
age2 = input("second age")
age3 = input("third age")

min_age = min(age1, age2, age3)
max_age = max(age1, age2, age3)

#this is the max age
print("max age is ", max_age)

#get the middle age
if age1 != max_age and age1 != min_age:
    print("middle age is age1 ", age1)
if age2 != max_age and age2 != min_age:
    print("middle age is age2 ", age2)
if age3 != max_age and age3 != min_age:
    print("middle age is age3 ", age3)

#this is the min age
print("min age is ", min_age)



# ---------second solution---------------
age1, age2, age3 = input(), input(), input()
age_list = [age1, age2, age3]

sorted_age_list = sorted(age_list)

first_age = sorted_age_list[0]
second_age = sorted_age_list[1]
third_age = sorted_age_list[2]


print(
    "this is the min",first_age,
    "this is the middle ", second_age, 
    "this is the max ", third_age
)


# def coffeMachine(coffe, suger, water, milk):
#     if milk > 0:
#         ourCoffe = coffe + suger + water + milk
#     else:
#         ourCoffe = coffe + suger + water
#     return ourCoffe

# mycup = coffeMachine(10, 10, 10, 0)
# print(mycup)


x = int(input("input something"))

if x > 10 and x > 1:
    print("its more than 10")
    print('its more than 1 also')
else:
    print('its not more than 10')

