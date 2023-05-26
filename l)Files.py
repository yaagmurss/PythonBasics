import os
import shutil

############### FILE EXISTS ####################

folderPath = "C:/Users/200741/Desktop/Docs"
filePath = "C:/Users/200741/Desktop/Docs/test.txt"
copyFilePath = "C:/Users/200741/Desktop/Docs/copy.txt"

if os.path.exists(folderPath):
    print("Path exists")
else:
    print("Path is not exists.")
if os.path.isfile(folderPath):
    print("This is a file.")
elif os.path.isdir(folderPath):
    print("This is a folder.")

############## READ A FILE ####################

try:
    with open(filePath) as file:
        result = file.read()
        print(result)
except FileNotFoundError:
    print("File not found")

############## WRITE A FILE ###################

text = "This is a some new text."
with open(filePath, "w") as file:
    file.write(text)


############### COPY A FILE ###################

# copyfile() = copies contents of a file
# copy() = copyfile - permission mode - destination can be directory
# copy2() = copy() + copies metadata (file's creation and modifications times )
shutil.copyfile(filePath, copyFilePath)


############## MOVE FILE ########################

source = "C:/Users/200741/Desktop/TEST1/TEST.txt"
destination = "C:/Users/200741/Desktop/TEST2/TEST.TXT"
try:
    if os.path.exists(destination):
        print("There is already a a file there")
    else:
        os.replace(source, destination)
        print(source + " moved")
except FileNotFoundError:
    print(source + " was not found")


############## DELETE FILE ########################

testPath = "C:/Users/200741/Desktop/TEST2/TEST.TXT"
try:
    os.remove(testPath) # delete a file
   # os.rmdir(testPath) #delete a file or empty folder
   # shutil.rmtree(testPath) #delete files and folders
    print("File deleted")

except FileNotFoundError:
    print("That file not found")
except PermissionError:
    print("you do not have permission to delete this file")
except OSError:
    print("That folder contains files")























