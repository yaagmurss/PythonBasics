# Function
# A block of code which is executed only when it is called

def hello(firstName, lastName, age):
    print("Hello " + firstName + " " + lastName)
    print("You are " + str(age) + " years old")
    print("Have a nice day")

hello("Yagmur", "Solmaz", 26)

# Return statement =
# Functions send Python values/objects back to caller
# These values/objects are known as the functions return value

def multiple(number1, number2):
    result = number1*number2
    return result
print(multiple(5,6))


# Keyword Arguments
# Arguments preceded by an identifier when we pass them to a function
# The order of arguments does not matter

def heloo(firstName, middleName, lastName):
    print("Hello, " + firstName + " " + middleName + " " + lastName)

heloo(lastName="Solmaz", middleName="No middle name", firstName="Yagmur")


#Scope
#The reqion that a variable is recognized
#A variable is only avaible from inside the region it is created
#A global and locally scoped versions of a variable can be created
#First local then enclosing then Global then Built in functions avaible


# *args
# Parameter that will pack al arguments into a tuple
# Useful so that a function accept varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))

def addStuff(*stuff):
    sum = 0
    stuff = list(stuff)
    for i in stuff:
        sum += i
    return sum

print(addStuff(1,2,3,4,5,6))


# **kwargs
# Parameter that will pack all arguments into a dictionary
# Useful so that a function can accept a varying amount of keyword arguments

def greet(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

greet(title = "Mrs", firstName = "Yagmur", lastName = "Solmaz")


def greet(**names):
    print("Hello", end=" ")
    for key, value in names.items():
        print(value, end=" ")

greet(title = "Mrs", firstName = "Yagmur", lastName = "Solmaz")










