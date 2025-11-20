import json

students={'student1':{'roll':101,'name':'Jhon','percent':98.5},
          'student2':{'roll':102},'name':'carol','percent':92.5,
          'student3':{'roll':103},'name':'Alice','percent':81.5
          }
print(students)
print(type(students))

#dump() - Writing/Civilization

with open("student_data.json","w") as fh:
    json.dump(students,fh,indent=4)

#load() - Reading the file/decivilizaation
with open("student_data.json","r")as fh:
    data=json.load(fh)

print(data)
print(type(data))

#update()
with open("student_data.json","r")as fh:
    data=json.load(fh)
    data.update(students)

#update operation
data.update(students)

with open("student_data.json",'w') as fh:
    json.dump(data,fh,indent=4)