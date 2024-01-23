## stacks can be implemented with python lists
some_stack = []
some_stack.append(3)
some_stack.append(7)
some_stack.pop()
print(some_stack)
if not some_stack:
    print(some_stack[-1])

## queues
## realized as a module in python
## first in first out 

import queue 

my_queue = queue.Queue()
some_list = [10, 20, 30, 40, 50]
for number in some_list:
    my_queue.put(number)


## last in first out can also be created
my_lifo_queue = queue.LifoQueue()
scores = [3,3,5,8,7,6,10]
for i in scores:
    my_lifo_queue.put(i)



