# writ a program that will ask for the user's name and password if inputted password is "mentors" print (welcome [username])
# if not print (access denied)
username = input("Enter your name: ")
password = input("Enter your password: ")
if password == "mentors":
    print(f"Welcome {username}")
else:
    print("Access denied")

#write a program to accept user input for a number and find the largest,
numbers = [2, 3, 4, 1]
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
print(f"The largest number is {max(numbers)}")

# change the following to a float 2,5,6,3,4
numbers = [2, 5, 6, 3, 4]
float_numbers = [float(num) for num in numbers]