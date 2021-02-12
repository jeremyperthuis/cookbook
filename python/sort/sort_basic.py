from operator import itemgetter, attrgetter
"""
BASIC SORTING MANIPULATIONS
"""

# 1. sort function (takes list)
l = [5, 19, 2, 76, 1, 3, 15, 18]
l.sort()
print(l)

# 2. sorted function (takes iterable)
l1 = [5, 19, 2, 76, 1, 3, 15, 18]
d1 = {'a': 3, 'b': 14, 'e': 2, 'f': 54}
print(sorted(l1, reverse=True))
print(sorted(d1))

# 3. sorted function on complex objects with lambda
t1 = [('franck', 15, 'A'),
      ('marie', 4, 'C'),
      ('steven', 63, 'F'),
      ('rob', 34, 'B'),]

print(sorted(t1, key=lambda x : x[2])) # list sorted by tuple's third index
print(sorted(t1, key=lambda x : x[1])) # list sorted by tuple's second index

# 4. sorted function with named attributes and operator module
class Human :
    def __init__(self, name, notation, age):
        self.name = name
        self.age = age
        self.notation = notation

    def __repr__(self):
        return repr((self.name, self.age, self.notation))

human_list = [Human('franck', 'A', 23),
              Human('ulysse', 'A', 12),
              Human('rob', 'C', 5),
              Human('laure', 'D', 34)]

print(sorted(human_list, key=lambda x : x.age))
print(sorted(human_list, key=lambda x : x.notation))


print(sorted(human_list, key=attrgetter('age')))
print(sorted(human_list, key=attrgetter('notation','age'))) #sort by notation and then by age
