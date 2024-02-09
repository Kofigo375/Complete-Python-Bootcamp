import re
pattern = "number"

text = "His phone number is 408-555-1234. Call phone Soon!"
print("phone" in text)
match = (re.search(pattern,text))
print(match.span())
print(match.start())
print(match.end())

matches  = re.findall("phone",text)
print(matches)

for match in re.finditer("phone",text):
    print(match.group()) 

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phone)
print(phone.group())