def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(5))

def create_squares(n):
    for x in range(n):
        yield x**2

print(create_squares(55))
print(list(create_squares(6)))


def gen_fibo(n):

    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+b

for num in gen_fibo(15):
    print(num)

## generator comprehension 
some_list = [2,3,4,5,6,7,8,9,10]
gen_comp = (item for item in some_list if item %2 == 0)
for i in gen_comp:
    print(i)