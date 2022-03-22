"""
BASIC DICTIONARY MANIPULATIONS
"""

d1 = {'name': 'frank', 'age': 34}

# 1. Access value using key
value = d1['name']

# 2. Insert key/value
d1['job'] = 'thief'

# 3. Update value using key
d1['age'] = 45

# 4. Delete key/value
del d1['job']

# 5. Iteration through loops
for key, value in d1.items():
    print(key, value, sep=' : ')

# 6. Iteration through Lambda Expression
print([key for key in d1])
print([(k,v) for k,v in d1.items()])

# 7. remove all items
d1.clear()


d2 = {'France': 'Paris',
      'Allemagne': 'Berlin',
      'Espagne': 'Madrid',
      'Belgique': 'Bruxelles'}

# 8. Get value without error
try:
    print(d2['Pologne'])
except KeyError :
    print(d2.get('Pologne'))

# 9. Remove key if present, and return value
print(d2.pop('France'))

# 10. Remove the last key/value, and return it as a tuple
print(d2.popitem())

# 11. Merge 2 dictionaries
d3 = {"a":{"b":1}}
d4 = {"c":2}
d3.update(d4)


# 12. Call __dict__ method in class
class testObject():
    def __init__(self):
        self.variable1 = "Value1"
        self.variable2 = "Value2"

t = testObject()
print(t.__dict__)

#13 Dict assignation
d5 = {"object1": {"sub1": "val1", "sub2":"val2"}}
d6 = {}
d7 = {}
d7["obj"] = d6["obj"] = d5["object1"]["sub1"]

#14 Join value as String
d8 = {"test": "value", "test2": "value2"}
print(','.join(list(d8.values())))
