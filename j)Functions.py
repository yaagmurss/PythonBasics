############## Function #############

def hello(firstName, lastName, age):
    print("Hello " + firstName + " " + lastName)
    print("You are " + str(age) + " years old")
    print("Have a nice day")

hello("Yagmur", "Solmaz", 26)

############## Return statement ############

def multiple(number1, number2):
    result = number1*number2
    return result
print(multiple(5,6))


############## Keyword Arguments #############

def heloo(firstName, middleName, lastName):
    print("Hello, " + firstName + " " + middleName + " " + lastName)

heloo(lastName="Solmaz", middleName="No middle name", firstName="Yagmur")

############## *args #############

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


############## **kwargs #############

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










