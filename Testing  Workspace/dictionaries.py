# A dictionary is a collection whch is unordered, unchangeable and indexed. No duplicate members.
'''
# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age':30
}
#print(person, type(person))

#Get Value

print(person['first_name'])
#print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

print(person)

#Get dictionary keys
print(person.keys())

#Get dictionary keys
print(person.items())

#Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

print(person2)

#Remove item
del(person['age'])
person.pop('phone')
print(person)

#Get length
print(len(person2))

#clear
#person.clear()

#list of dictionaries
'''


people = [
    {'name':'Martha', 'age': 30},
    {'name':'Kevin', 'age': 25}
]

print(people[1]['name'])