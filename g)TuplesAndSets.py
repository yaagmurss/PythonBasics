############ TUPLE ############
#unordered and unchangeable

student = ("yagmur", 21, "female")

print(student.count("yagmur"))
print(student.index("female"))

for i in student:
    print(i, end="-")


############# Set ###########
# unordered, unindexed, no duplicate values

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