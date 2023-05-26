############# While Loop ##################

name=""
while len(name)==0:
    name = input("Enter your name:")
print("Hello " + name)


############# For Loop#############

for i in range(10):
    print(i)

for i in range(50, 100+1, 2):
    print(i)

for i in "Hello world":
    print(i)

for i in range(500, 100, -20):
    print(i)

############## Nested loops #############

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use? ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()


# break = use "break" in order to exit from loop
# continue = use "continue" in order to skip iteration
# pass = does nothing act as a placeholder

############## Break #############
while True:
    name = input("Please enter your name:")
    if name!="":
        break

############## Continue #############
phoneNumber = "123-456-789"
for i in phoneNumber:
    if i == "-":
        continue
    print(i, end="")

############## Pass #############
for i in range(15):
    if i == 5:
        pass
    else:
        print(i, end="-")















