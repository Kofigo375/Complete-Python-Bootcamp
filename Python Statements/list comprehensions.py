## inefficient  way of populating a list
string1 = 'hello'

emptlist = []
for chars in string1:
    emptlist.append(chars)

print(emptlist)

## using list comprehension to achieve the same result efficiently
efflist = [chars for chars in string1]
print(efflist)
 
numlist = [num**2 for num in range(2, 39)]
print(numlist)