#If Statement

#Example 1#
age = int(input("How old are you?"))

if age <= 18:
    print("You are a child")
elif age > 100:
    print("You are too old")
else:
    print("You are an adult")


#Example 2#
temp = int(input("What is temperature today?"))

if temp>=0 and temp<=30:
    print("Go outside")
else:
    print("Stay at home")