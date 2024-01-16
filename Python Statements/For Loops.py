## tuple unpacking : can be used to obtain data from a list of tuples
mylist = [(2,3), (7,8), (0,9)]
for a,b in mylist:
    print(a)
    print(b)

for item in mylist:
    print(item)

for a,b in mylist:
    print(b)

## iterating through a dictionary
## by default, iterating through a dict only iterate through the keys
mydict = {"k1":1, "k2":2, "k3":3, "k4":4}
for item in mydict:
    print(item)

## you can iterate through the (key,value) pairs 
for item in mydict.items():
    print(item)

## to apply the tuple unpacking to a dictionay
for (key,value) in mydict.items():
    print(key)
    print(value)

## dictionaries are unordered 
## only the values can be extracted from a dictionary
for values in mydict.values():
    print(values)