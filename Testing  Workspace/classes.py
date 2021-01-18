#a class is like a blueprint for creating objects. An objects has properties and methods
#(functions) associated with it. Almost everything isn python is an object

#creating a class
class User:
    #constructor
    def __init__(self, name, email, age):
        self.name=name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

#Extending class

class Customer(User):
     #constructor
    def __init__(self, name, email, age):
        self.name=name
        self.email = email
        self.age = age
        self.balance=0
    
    def set_balance(self, balance):
        self.balance = balance
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is ${self.balance}'



#init user object
brad = User('Bradyy', 'bebe@gmail.com', 37)

#Init customer object
janet=Customer('Janet', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
print(brad.greeting())