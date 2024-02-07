from collections import Counter
from collections import defaultdict
from collections import namedtuple

my_list = [1,1,1,1,1,2,2,2,2,2,3,3,3,3]

counted = Counter(my_list)
print(counted)

d = {'a':10}
#print(d["wrong"])

d_d = defaultdict(lambda:0)
d_d["correct"] = 100

Dog = namedtuple("Dog", ['age', 'breed', 'name'])
sam = Dog(age=10, breed='sakraman', name='sam')
print(type(sam))