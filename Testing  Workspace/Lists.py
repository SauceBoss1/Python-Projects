#Here I'll be practicing my list skills

#create a list
numbers = [1, 2, 3, 4, 5]
#use a constructor
#numbers2= list((1, 2, 3, 4)) worst way to create a list

fruits= ['Apple', 'Oranges', "Grapes", 'Pears']


# get a value (remember everything starts at 0)
print(fruits[1])

#get length
print(len(fruits))

# Append
fruits.append('Mangos')

print(fruits)

# remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, "Strawberries")
print(fruits)

# Remove with pop
fruits.pop(2)
print (fruits)

#reverse a list
fruits.reverse()
print(fruits)

#sort list
fruits.sort()
print(fruits)

#reverse sort list
fruits.sort(reverse=True)
print(fruits)

#change value
fruits[0] = 'blueberries'