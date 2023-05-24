import os

#File.Exists

path = "C:/Users/500500/Desktop/Docs"

if os.path.exists(path):
    print("Path exists")
else:
    print("Path is not exists.")

if os.path.isfile(path):
    print("This is a file.")
elif os.path.isdir(path):
    print("This is a folder.")

#https://www.youtube.com/watch?v=XKHEtdqhLK8&list=RDCMUC4SVo0Ue36XCfOyb5Lh1viQ&start_radio=1
#02:04:33