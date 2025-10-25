#pathlib.Path.exists()

from pathlib import Path

file_name=Path("C:/Users/saqui/Desktop/py/practice_1.txt")

if file_name.exists():
    print("File exists.")
else:
    print("File does not exist,creating it.")
    fh=open(file_name,'xt')
    fh.write("SOme Content")

    fh.close()

