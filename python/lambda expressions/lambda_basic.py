"""
LAMBDA EXPRESSIONS EXAMPLES
"""

# 1. Add 2 variables
add = lambda x, y : x + y
print(add(5,8))

#2. Immediately invoked lambda expression
print((lambda x : x*x)(3))
print((lambda x, y : x * y)(3,7))
print((lambda *args : sum(args))(5,7,3))
print((lambda **kwargs : sum(kwargs.values()))(one=1, two=3, five=5))

# 3. Use with map, filter
l1 = list(map(lambda x : x.upper(), ['test', 'chien']))
print(l1)

l2 = list(filter((lambda x : 'x' in x), ['xavier', 'franck', 'xylophone']))
print(l2)

# 4. Sorting
l3 = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(sorted(l3))

integer_sorted = sorted(l3, key=lambda x: int(x[2:]))
print(integer_sorted)


l4 = [{"a":45, "b":87}, {"a":26, "b":43}]
l4_res = list(map(lambda x : x["a"], l4))
print(l4_res)
