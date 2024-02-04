## decorators allows you to add more code 
## to an existing function

def func():
    return 1

def hello(name="Jose"):
    print("The hello() function has been executed!")

    def greet():
        return ("\t This is the greet() func inside hello!")

    def welcome():
        return ("\t This is welcome inside hello")

    print("I will return a fucntion")

    if name == "Jose":
        return greet
    else:
        return welcome


my_new_func = hello("Jose")

print(my_new_func())

def cool():

    def super_cool():
        return 'I am very cool'
    
    return super_cool

some_func = cool()

print(some_func())

def Hi():
    return "Hi Ephraim !"

def other(some_def_func):
    print("other code runs here!")
    print(some_def_func())

other(Hi)

## we can return a function 
## we can have a fucntion as an argument


def new_decorator(original_func):

    def wrap_func():
        print("Some extra code, before the original function")
        original_func()
        print("Some extra code, after the original fucntion")

    return wrap_func


@new_decorator  ## this decorator acts as an ON/OFF  swith the that wraps
def func_need_dec(): ## the new_decorator over the func_need_dec
    print("I want to be decorated! ")

func_need_dec()