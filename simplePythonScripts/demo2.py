import json

a = 'sring'
b = 25
c = 17.3
d = [2, 3, 5, 6, 7]
e = (7, 3, 5, 6, 2)
f = {2,5, 3, 7, 6}
x = {'name':'Miano', 'age':25, 'gender':'F', 'Nationality':'Cameroon'}

y = json.dumps(x)

with open('demo.jeson', 'w') as fh:
    fh.write(json.dumps(a))
fh.close()

fh =open('demo.jeson', 'r')
print(fh.read())
fh.close()

