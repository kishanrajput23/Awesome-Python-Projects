import json

a = 'sring'
b = 25
c = 17.3
d = [2, 3, 5, 6, 7]
e = (7, 3, 5, 6, 2)

#a set cannot be converted into json
f = {2,5, 3, 7, 6}

x = {'name':'Miano', 'age':25, 'gender':'F', 'Nationality':'Cameroon'}

print(json.dumps(x))
print("-------------------------------")

print(json.dumps(e))
print("-------------------------------")

print("indent 3 json fomat",json.dumps(d, indent=3))
print("-------------------------------")

print("indent 2 json fomat",json.dumps(d, indent=2))
print("-------------------------------")

print("indent 1 json fomat",json.dumps(e, indent=1))
print("-------------------------------")

print("indent 0 json fomat",json.dumps(e, indent=0))
print("-------------------------------")

print("separator for dictionary in json fomat",json.dumps(x, separators=("; ","=")))
print("-------------------------------")

#creating a JSON file  storing data in
with open('demo.jeson', 'w') as fh:
    fh.write(json.dumps(a))
fh.close()

#Opening JSON file in Read mode and read from it
fh =open('demo.jeson', 'r')
print(fh.read())
fh.close()

