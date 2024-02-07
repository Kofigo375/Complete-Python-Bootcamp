## the map() function can be used to apply a function
## to each element in a list 

def square(num):
    return num ** 2

my_list = [2,4,5,6,7,1,3]
for item in map(square, my_list):
    print(item)

## if you want the list back
squared_list = list(map(square, my_list))
print(squared_list)

## filter() is quite nalogous to map()
## the key difference is that the function inside
## the filter method/function must return a bool.

def check_even(num): 
    return num%2 == 0

filtered_list = list(filter(check_even, my_list))
print(filtered_list)

## lambda expression / anonymous function

cubed_list = list(map(lambda num: num ** 3, filtered_list))
print(cubed_list)