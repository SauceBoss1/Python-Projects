# A Tuple is a collection which is ordered and unchangable.
'''
#creating a tuple

fruits = ('Apple', 'Oranges', 'Grapes')

#a single value tuple needs a trailing comma
fruits2 = ('Apples',)

#get a value
print(fruits[1])


#this is illegal b/c u cant change items in tuples
#fruits[0] = 'Pears'

# Delete tuple
#del fruits2



#length
#print(len(fruits))

'''

#SETS: A set is a collection which is unordered and unindexed. Nu duplicate members

# Create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}

#Check if in set

print('Apples' in fruits_set)

#Add to set
fruits_set
fruits_set.add('Grape')

print(fruits_set)

# remove from set
fruits_set.remove('Grape')

#Add duplicate (doesnt do anything)
fruits_set.add('Apples')

#Clear set
#fruits_set.clear()

print(fruits_set)

#delete
#del fruits_set