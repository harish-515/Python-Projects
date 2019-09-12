import datetime
print("The Date and Time is",datetime.datetime.now())
from os import path

file_path = path.relpath("AddedFiles/fruit.txt")

myfile = open(file_path,"r")
content = myfile.read()
myfile.close()

with open(file_path,"r") as myfile1:
    content = myfile1.read()

print(content)    