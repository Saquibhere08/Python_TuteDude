dictionary = {'a':'apple','b':'banana','c':'cat'}
dictionary['d']='dog' #Add function

print(dictionary)

del(dictionary['c']) #Delete Function
print(dictionary)

print('b' in dictionary) #It will only show True or False
print('e' in dictionary)  #We know weather a value is present or not
print(dictionary.values()) #To show only the values not the keys

print(dictionary.get('b'))
print(dictionary.get('g')) #To get the values present in the dictionary or not
