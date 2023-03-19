from functools import *
a = [1, 2, 3, 4]
c = ['khskdf', 'jfsdcjlk', 'g']
b = list(map(lambda x: x[0], c))
t = reduce(lambda x, y: x+y, a)
print(t)
