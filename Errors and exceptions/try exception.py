# def add_two(num1, num2):
#     print(num1+num2)

# add_two(200, 30)
# num1 = 20
# num2 = input("please enter a number: ")

# add_two(num1,num2)
# print("Something happend!")

## general sytax of try and except

try:
    # what we want to try..
    # there can be an error or not
    result = 10 + '10'
except:
    ## when an error happens in try execute this
    print("looks like you aren't doing the right thing")
else:
    # execute when there is no error in try 
    print("Add successful! ")

def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Ooops! that was not a number")
            continue
        else:
            print("yes thank you ")
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end")
ask_for_int()

