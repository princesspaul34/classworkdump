"""
Mini Project after the completion of comments, Variable, Operators[Arithmetics, Comparison,
Logic, Assignment], simple if-else.
"""
"""
Answers Below
"""
# open file with a or w

name = input("Enter your name: ")
print("Hello, " + name)

x = float(input("Enter first number (x): "))
y = float(input("Enter second number (y): "))
subpage = "Addition of two values x and y : ",x + y

print(x - y)

product = x * y
print(product)

print(x / y)

age = float(input("Enter your age: "))
print(int(age) >= 18)

math_score = float(input("Enter your Math score: "))
english_score = float(input("Enter your English score: "))
print(math_score > 50 and english_score > 50)

is_logged_in = str(input("Are you logged in? (yes/no): ")) == "yes"
print(not is_logged_in)

is_raining = str(input("Is it raining? (yes/no): ")) == "yes"
has_umbrella = str(input("Do you have an umbrella? (yes/no): ")) == "yes"
print(is_raining or has_umbrella)

number = float(input("Enter a number to check if it's even: "))
print(int(number) % 2 == 0)

score = float(input("Enter your score: "))
if score >= 50:
    print("Congratulations {name} you Pass with Score: {score}")
else:
    print("Ops! {name} you Fail with Score: {score}")

temp = float(input("Enter temperature: "))
if int(temp) > 30:
    print("The Temperature is very Hot - UV")
else:
    print("Awesome the Temperture is Cool")

count = float(input("Enter a count number: "))
count += 10
print(count)

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
print(a != b)

status = str(input("Enter status (active/inactive): "))
if status == "active":
    print("You are very Welcome {name}")
else:
    print("Ops! Access denied for you {name}")

time = float(input("Enter time in 24hr format: "))
if int(time) < 12:
    print("Good morning")
else:
    print("Good afternoon")

m = float(input("Enter value for m: "))
n = float(input("Enter value for n: "))
temp = int(m)
m = int(n)
n = temp
print(m, n)

marks = float(input("Enter your marks: "))
if int(marks) > 80:
    print("Excellent")
else:
    print("Keep trying")

p = float(input("Enter number p: "))
q = float(input("Enter number q: "))
print(p % 2 == 0 and q % 2 == 0)

food = str(input("What food do you want?: "))
if food == "rice":
    print("Eat rice")
else:
    print("Choose something else")

with open("miniprojectResult.txt", "a") as f:
    f.write("Mini Project after the completion of comments, Variable, Operators[Arithmetics, Comparison,Logic, Assignment], simple if-else.")
