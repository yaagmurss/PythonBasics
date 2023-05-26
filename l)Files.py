import os
import shutil

# File.Exists

folderPath = "C:/Users/500500/Desktop/Docs"
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

# Read a file

try:
    with open(filePath) as file:
        result = file.read()
        print(result)
except FileNotFoundError:
    print("File not found")


# Write a file

text = "This is a some new text."

with open(filePath, "w") as file:
    file.write(text)


# Copy File

# copyfile() = copies contents of a file
# copy() = copyfile - permission mode - destination can be directory
# copy2() = copy() + copies metadata (file's creation and modifications times )


shutil.copyfile(filePath, copyFilePath)
