#os.path.exists
import os

file_name="C:/Users/saqui/Desktop/py/practice.txt"

if os.path.exists(file_name):
    print("File exists.")
else:
    print("File does not exist.")
