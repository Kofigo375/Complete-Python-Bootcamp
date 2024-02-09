import time
import timeit

## Start time
## Your code
## End time

def func_one(n):
    return [str(n) for n in range(n)]


def func_two(n):
    return list(map(str,range(n)))


start_time = time.time()
result = func_one(10)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

stmt = '''
func_one(100)'''

setup = '''
def func_one(n):
    return [str(n) for n in range(n)]
'''

print(timeit.timeit(stmt,setup,number=100000))

stmt2 = ''' 
func_two(100)'''

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
print(timeit.timeit(stmt2,setup2,number=100000))