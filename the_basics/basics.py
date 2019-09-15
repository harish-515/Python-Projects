import datetime

"""
print("The Date and Time is",datetime.datetime.now())
from os import path

file_path = path.relpath("files/fruit.txt")

myfile = open(file_path,"r")
content = myfile.read()
myfile.close()

with open(file_path,"w") as myfile:
    myfile.write("Tomato n Cucumber n Onion")

with open(file_path,"r") as myfile1:
    content = myfile1.read()

print(content)    

with open("files/fruits.txt","x") as myfile2: 
    myfile2.write("Okra") 

"""

'''  Text Appending to a File
with open("files/data.txt","a+") as data:
    data.seek(0)
    ctnt = data.read()
    data.seek(0) 
    data.write("\n" + ctnt)
    data.write("\n" + ctnt)
'''
"""
System Modeules
import sys
sys.builtin_module_names


import time
import os
while True:
    if os.path.exists("files/vegetables.txt"):
        with open("files/vegetables.txt") as vegs:
            print(vegs.read())
    else:
        print("File does not exist.")        
    time.sleep(10)
"""

"""
Third - Party Modules
Read the temp today and calculate the average of the temperatures

Using : pandas

import time 
import os
import pandas

while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist.")        
    time.sleep(10)

"""