#Tuple = collection which is unordered and unchangeable
#                       used to group together related data

student = ("Bro", 21, "male")

print(student.count("Bro"))
print(student.index("male"))

for i in student:
    print(i, end="-")


#Set = collection which is unordered, unindexed, no dublicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#dishes.update(utensils)
dinnerTable = utensils.union(dishes)

for i in dinnerTable:
    print(i)

print(dishes.difference(utensils))
print(utensils.intersection(dishes))