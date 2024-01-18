## a class is like a template/blueprint that defines how 
## a future object/instance will be

class SampleWord(): 
    pass

class Dog():
    # CLASS OBJECT ATTRIBUTES
    # SAME FOR ALL INSTANCES
    species = 'mammal'

    ##               argument
    def __init__(self, breed,name,spots):
        ##  assigning argument to attribute
        self.breed = breed
        self.name = name
        self.spots = spots

    # Methods ---> like a function inside a class 
    def bark(self):
        print("Wow wow wow!")
    
my_dog = Dog(breed = 'Chihuahua', name = 'nick', spots=True)
my_dog.bark()



