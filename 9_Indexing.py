#Index operator [] = gives access to a sequence's element (str,list,tuples)

name = "Bro Code!"

if(name[0].islower()):
    name = name.capitalize()

firstName = name[:3].upper()
lastName = name[4:].lower()
lastCharacter = name[-1]

print(firstName)
print(lastName)
print(lastCharacter)
