"""
User Input
Using if condition with logic operators
"""
print("Print my name: ")
# name1 = "Samuel"
name1 = input("Please enter your name: ")
print("Hi Welcome ",name1)
print("\n Lets perform simple operation:")
# Simple multiplication result=x*y
x =float (input("Please enter value for X: "))
y= float(input("Please enter value for Y: "))

# Extracting only integer value for mulitiplication
result =int(x) *int(y)
print("Congratulation your result in Integer is : ",result)

# Implement direct float figure as entered
result1 = x*y
print("Congratulation your result in Float is : ",result1)

# if condition
print("\n If condition___________________")
if x>y:
    result = x/y
    print("X is greater than Y here is Simple Division of X/Y :", result)
else:
    result = x*y
    print("Because X is less than Y, here is Simple Multiplication of X*Y :", result)