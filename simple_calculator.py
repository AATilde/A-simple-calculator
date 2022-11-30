print("Welcome to my simple calculator")
# User will enter the operation he wanted to perform
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
# collecting input from user
user_input = input("Select your the operation you want to perform from 1-4: ")
# printing which operation you want to perform
if user_input == '1':
    print("you are performing Addition")
elif user_input == '2':
    print("You are performing Subtraction")
elif user_input == '3':
    print("You are performing Multiplication")
elif user_input == '4':
    print("you are performing Division")
# if any number more than 4 is entered
else:
    print("invalid input")
# collecting two numbers from user to perform operation which user has selected
x = float(input("Enter your first number: "))
y = float(input("Enter your second number: "))
# printing result after recieving two numbers
if user_input == '1':
    add = x+y
    print("your result is", add )
elif user_input == '2':
    sub = x-y
    print("your result is", sub )
elif user_input == '3':
    mul = x*y
    print("your result is", mul )
elif user_input == '4':
    div = x/y
    print("your result is", div )