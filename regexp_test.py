import re
with open ('test.txt') as f:
    txt = f.read()

lst1 = txt.split(' ')
print(lst1)
lst2 = re.split(r'\W+', txt)
print(lst2)
lst3 = re.split(r'[,.;&! ]', txt)
print(lst3)
lst4 = re.split