# input password and username
password = input("Enter password: ")
if password == "mentors":
    # access granted
    print("welcome")
else:
    print("access denied")

name = input("Enter username: ")
if name == "mentors":
    print("access granted")
else:
    print("access denied")

# write a program to accept user input for a number and find the largest
numbers = [4, 5, 6, 7, 8, 10]
user_number = int(input("Enter a number: "))
largest = max(numbers + [user_number])
print("The largest number is:", largest)   

