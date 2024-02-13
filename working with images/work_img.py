from PIL import Image
mach = Image.open("example.jpg")
print(type(mach))
print(mach.filename)
print(mach.size)


## cropping images 
print(mach.crop((0,0,100,100)).show())