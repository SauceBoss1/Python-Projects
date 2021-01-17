# a function is a block of code which only runs when it is called. In python, we do not use curly brackets, we use indentation with tables or spaces

#Create a function
def sayHello(name= 'Sam'): #name= sets a default
    print(f'Hello {name}')

sayHello(300)

#return values

def getSum(num1, num2):
    total = num1 + num2
    return total

num=getSum(3,4)
print(num)



#A lambda function is a small anonymous function.
#A lamda function can take any number of arguments, but can only have one expression.
getSum = lambda num1, num2 : num1 + num2
print(getSum(10,3))
