## general syntax:
def function_name():
    '''
    Docstring which explains what's inside 
    the function
    '''
    print("Hello world")

function_name()

## illustration of positional arguments
def sum_func(a,b):
    '''
    Returns 5% of the sum of a and b
    '''
    return sum((a,b)) * 0.05
print(sum_func(9,10))

## Illustration of *args
## *args allows multiple(as many as user enters) arguments to be entered
## the arguments are treated as tuples inside the funcion
def sum_func_2(*args):
    for items in args:
        print(items)

sum_func_2(4,5,6,7,8,9,10)

## **kwargs
## allows as many arguments from the user
## arguments are treated as a dictionary

def func(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    else:
        print('I did not find any fruit here')

func(salab = 'cream', name = 'osei', fruit = 'orange')
## args and kwargs are just conventions
## what actually makes the difference is the * and **

## *args and **kwargs can be used together
def func_one(*args, **kwargs):
    print(f"I would like {args[0]} and {kwargs['food']}")

func_one(3,77,66, fruit = 'orange', food = 'eggs')



