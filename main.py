# How to open read and write files in python

with open('names.txt','+') as textFile:
    textFile.write("Hello from the computer")
    print(textFile.read())
