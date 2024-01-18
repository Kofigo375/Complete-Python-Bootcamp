## Inheritance is a way to form new classes 
## with classes already defined.

# base class
class Animal():

    def __init__(self):
        print("ANIMAL CREATED")
        
    def who_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print("I am eating")
# derived class
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

my_dog = Dog()