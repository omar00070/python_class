from packages.package1 import addition

# we neeed to add 2 numbers from an input for a user
n1 = int(input("please input a number "))
n2 = int(input("please input a second number "))

added = addition(n1, n2)

print('the added number is', added )