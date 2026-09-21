"""
2nd July 2025
Class 3 
Syntax, variale, data types
"""

# Syntax is machine readable word or statements
print("my name id : Paul")

# Variable definition
name1 = "samuel" # Asigning name samuel to name1 samuel is in quoation because it is a string
num = 3 # Assigning number 3 to num and this is an integer no need for quotation
num2 = 23.03859485 # Assigning number with decimal place to num2 this is float with no need for quotation
print(num2)
_num3 = 2/4
numFraction = 4/5
print(_num3)

#List
genderList = ["Male", "Female"]
nameList = ["Samuel", "Daliya", "Arib", "Vivian", "Salvation"]
numList = [23, 25.34, 26, 90]
print(numList)
# Dictionary
schoolDict = {"key":"value", "key2":"value2", "key3":"value3"}
personDict ={"name":"Daliya", "location":"Dougirei", "school":"Army School", "gender": "male", "age": 35}
print(personDict)

# printout single element from a dictionary
print("\n new school \n")
print(personDict["school"])
print(" new school printed above \n")

#Data Types Integer, Boolean, Float, string, List, Dictionary
# Construct 2  new variables for each for the following: list, dictionary, float and string explained datatypes

# indexing
nameList = ["Samuel", "Daliya", "Arib", "Vivian", "Salvation"]
# numbering = [   1,       2         3          4         5    ]
# Post/index = [   0,         1        2        3          4   ]

print("name is : ", nameList[2])

condition = True
condition2 = False
# print()  show the result of an action or variable
# type()  get the type of a variable

# Verify the data types
print("checking the datatype of", name1," :::",type(name1))
print("checking the datatype of", nameList," :::",type(nameList))
# class work
# verify the datatype for num, num1, genderList, numList, schoolDict, personDict, condition, and condition2




