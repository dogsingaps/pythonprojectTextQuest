import re
a = "abc123"
b = "123abc"


p1 = "\d{1,3}?"
result1 = re.search(p1, a)
if result1:
    print(result1)
else:
    print('no match')
