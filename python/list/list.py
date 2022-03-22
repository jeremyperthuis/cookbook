"""
BASIC LIST MANIPULATIONS
"""

# Merge 2 lists
list1 = ["object1", "object2", "object3"]
list2 = ["item1", "item2", "item3"]
list_merged = [*list1, *list2]

# Surround list element with special caracters
list3 = list(map(lambda x : f"({x})", list1))

# Group list by 4 element
list_a = [6108, '8', 'validated', '118132', 6175, '8', 'validated', '118697', 6199, '8', 'validated', '116149', 6268, '8', 'validated', '121323']
group = [list_a[n:n+4] for n in range(0, len(list_a), 4)]


# Difference between 2 listIds

list4 = ["a", "b", "c"]
list5 = ["a", "b", "c", "d"]
diff = list(set(list5)-set(list4))
