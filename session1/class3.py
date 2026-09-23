#write a program that will ask for user name and password if inuyyed password is mentors, priny welcome_(username) 
#if not print access denied

#write a program to accept user input for two numbers and find the largest

#change the following to a float 2,5,6,3,4

#1
Username = input("Enter your username: ")
Password = input("Enter your password: ")

if Password == "mentors":
    print("Welcome", Username)
else:
    print("Access Denied")

#2
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))

if input1 > input2:
    print("The largest number is:", input1)
else:
    print("The largest number is:", input2)

#3
numbers = [float(x) for x in input("Enter five numbers separated by commas: ").split(",")]
print("The 5 numbers in float format are:", numbers)
git init