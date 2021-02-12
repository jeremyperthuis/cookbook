"""
BASIC DICTIONARY MANIPULATIONS
"""
DELIMITER = '\n'+'—'*60+'\n'

d1 = {'name': 'frank', 'age': 34}
d2 = {'France': 'Paris',
      'Allemagne': 'Berlin',
      'Espagne': 'Madrid',
      'Belgique': 'Bruxelles'}


# 1. Access value using key
print(d1['name'],end=DELIMITER)

# 2. Insert key/value
d1['job'] = 'thief'
print(d1, end=DELIMITER)

# 3. Update value using key
d1['age'] = 45
print(d1,end=DELIMITER)

# 4. Delete key/value
del d1['job']
print(d1, end=DELIMITER)

# 5. Iteration through loops
for key in d1:
    print(key, d1[key], sep=' : ')

for key, value in d1.items():
    print(key, value, sep=' : ')

print(end=DELIMITER)

# 6. Iteration through Lambda Expression
print([key for key in d1])
print([(k,v) for k,v in d1.items()],end=DELIMITER)

# 7. remove all items
d1.clear()
print(d1, end=DELIMITER)

# 8. Get value without error
try:
    print(d2['Pologne'])
except KeyError :
    print(d2.get('Pologne'), end=DELIMITER)

# 9. Remove key if present, and return value
print(d2.pop('France'))
print(d2.keys(),end=DELIMITER)

# 10. Remove the last key/value, and return it as a tuple
print(d2.popitem())
print(d2.keys(),end=DELIMITER)

# 11. Merge 2 dictionaries
d1.update(d2)
print(d1,end=DELIMITER)