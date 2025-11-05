fh=open("Practice.txt","rt") #Should not open with 'wt' mode as it will overwrite the file
contents=fh.read()
fh.close()

print(contents)