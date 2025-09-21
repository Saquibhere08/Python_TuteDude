#string fuction 1
a='saquib'
print(a.capitalize()) #capitalize first word of the letter
print(a.upper()) #MAKES THE WHOLE STATMENT IN UPPERCASE
print(a.lower()) #makes the whole statement in lowercase

b='7'
print(b.isnumeric()) #Checks the value is numerical or not
print(b.isalpha()) #Checks if the value is alpha or not

c='Mike is a good boy'
print(c.startswith('Mike')) #Checks if the statment starts with a certain word
print(c.endswith('Boy')) #Checks if the statment ends with a certain word
print(c.replace('Mike','Saquib')) #Replaces a word with another
print(c.find('a')) #Checks if the required word is available or not

print(c.lstrip()) #removes the space at the starting of the sentence
print(c.split()) #spilts the above statment
print(c.splitlines())

d='Mike','Saquib'
print(d)
e=','
print(e.join(d))
