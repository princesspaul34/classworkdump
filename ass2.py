
#Mini Project after the completion of comments, Variable, Operators[Arithmetics, Comparison,
#Logic, Assignment], simple if-else.


 #Declare a variable called "name" to receive & store your first name from user then print a greeting with it.
name = input("Enter your first name: ")
 #Create two variables x and y and store any two numbers from user. Print the sum of x and y.
 x = 2
 y = 5
 print(x + y)
 #Using the same variables x and y, print their difference.
 print(x - y)
 #Multiply the two variables and store the result in a new variable called product. Print the result.
 product = x * y
 print(product)
 #Divide x by y and print the result.
 print(x / y)
 #Create a variable age and let user assign age. Check if the age is greater than or equal to 18 and print the result.
 age = int(input("Enter your age: "))
 if age >= 18:
     print("You are eligible to vote.")
 else:
     print("You are not eligible to vote.")
 #Create two variables math_score and english_score, each with values between 0 and 100. Check if both are above 50 and print True or False.
 math_score = int(input("Enter your math score: "))
 english_score = int(input("Enter your english score: "))
 if math_score > 50 and english_score > 50:
     print("Both scores are above 50.")
 else:
     print("At least one score is not above 50.")
 #Create a variable is_logged_in and set it to True. Use a logical NOT to print the opposite value.
 is_logged_in = True
 print(not is_logged_in)
 #Declare a variable is_raining as True and has_umbrella as False. Use logical OR to determine if you can go outside and print the result.
    is_raining = True
    has_umbrella = False
    if is_raining or has_umbrella:
        print("You can go outside.")
    else:
        print("You cannot go outside.")
 #Create a variable number and assign any integer. Check if the number is even using the modulo operator and print True or False.
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
 #Create a variable score and set it to a value between 0 and 100. Use an if-else statement to print "Pass" if the score is 50 or above and "Fail" otherwise.
    score = int(input("Enter your score: "))
    if score >= 50:
        print("Pass")
    else:
        print("Fail")
 #Declare a variable temp for temperature and check if it is above 30. If so, print "Hot", otherwise print "Cool".
 temp = int(input("Enter the temperature: "))
 if temp > 30:
     print("Hot")
 else:
     print("Cool")
 #Assign a value to a variable count. Add 10 to it using the assignment operator and print the updated value.
 count = 5
 count += 10
 print(count)
 #Set two variables a and b. Check if a is not equal to b and print the result.
 a = 5
 b = 10
 if a != b:
     print("a is not equal to b")
 else:
     print("a is equal to b")
 #Declare a variable status and set it to "active". Use an if-else to print "Welcome" if status is "active", otherwise print "Access denied".
 status = "active"
 if status == "active":
     print("Welcome")
 else:
     print("Access denied")
 #Create a variable time and assign a value in 24-hour format. If time is less than 12, print "Good morning", else print "Good afternoon".
 time = int(input("Enter the time in 24-hour format: "))
 if time < 12:
     print("Good morning")
 else:
     print("Good afternoon")
 #Declare two numbers m and n. Swap their values using a third variable and print the result.
 m = 5
 n = 10
 temp = m
 m = n
 n = temp
 print("After swapping:")
 print("m =", m)
 print("n =", n)
 #Create a variable marks and use an if-else to check if marks are greater than 80. Print "Excellent" if true, else print "Keep trying".
 marks = int(input("Enter your marks: "))
 if marks > 80:
     print("Excellent")
 else:
     print("Keep trying")
 #Assign values to two variables p and q. Check if both are divisible by 2 and print the result.
 p = 10
 q = 15
 if p % 2 == 0 and q % 2 == 0:
     print("Both p and q are divisible by 2.")
 else:
     print("At least one of p or q is not divisible by 2.")
 #Ask the student to choose any real-life decision (e.g., choosing what to eat) and use a simple if-else structure to model it in code
 food = input("What would you like to eat? ")