## the enumerate() function:
## takes an iterable(list, tuple etc..) and return the item and index postion.

name = 'Ephraim'
for item in enumerate(name):
    print(item)

for index,item in enumerate(name):
    print(index)
    print(item)
    print('\n')

## the zip() function:
## pairs lists into tuples

list_one = [1,1,3,4]
list_two = [2,3,4,6]

for item in zip(list_one, list_two):
    print(item)

## the in keyword can be used to check if an item 
## is in a list.. returns a bool
print(2 in [2,3,4]) 