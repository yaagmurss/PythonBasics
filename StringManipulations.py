name="hello world"

#len(name)
print("Length of the string is " + str(len(name)))

#name.find("o")
print("Index of first letter o is " + str(name.find("o")))

#name.capitalize()
print("Capitalized name is " + name.capitalize())

#name.upper()
print("Uppered name is " + name.upper())

#name.lower()
print("Lowered name is " + name.lower())

#name.isdigit()
print("Is name digit? " + str(name.isdigit()))

#name.isalpha()
print("Is name alpha? " + str(name.isalpha()))

#name.count()
print("Count of letter o is " + str(name.count("o")))

print((name + " ") *3)
