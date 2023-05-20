#While Loop#
#A statement that will execute it is block of code in a unlimited amount of time

name=""
while len(name)==0:
    name = input("Enter your name:")
print("Hello " + name)


#For Loop#
#A statement that will execute it is block of code in a limited amount of time

print("---------------------")
for i in range(10):
    print(i)
print("---------------------")
for i in range(50, 100+1, 2):
    print(i)
print("---------------------")
for i in "Hello world":
    print(i)
print("---------------------")

for i in range(500, 100, -20):
    print(i)
print("---------------------")

#Nested loops
#The inner loop will finish all of it is iterations before finishing one iteration of the outer loop.

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use? ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

# Loop Control Statements = change a loops execution from it is normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing act as a placeholder

#Break
while True:
    name = input("Please enter your name:")
    if name!="":
        break

#Continue
phoneNumber = "123-456-789"
for i in phoneNumber:
    if i == "-":
        continue
    print(i, end="")

#Pass
for i in range(15):
    if i == 5:
        pass
    else:
        print(i, end="-")















