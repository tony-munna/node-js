# s={}
# print(type(s))

# s={1,2,3,4,5}
# print(type(s))
'''
add
update
pop
remove
'''

'''no allows duplicate'''
# s={1,2,3,3,4,4,5}
# print(s)

'''unordered'''
# s={5,2,1,3,4,7,9,5,6}
# print(s)

# s={5,2,1,3,4,7,9,5,6}
# s.add(88)
# print(s)

# s={5,2,1,3,4,7,9,5,6}
# s.update({99,55,66,77})
# print(s)

# s={5,2,1,3,4,7,9,5,6}
# s.pop()
# print(s)

# s={5,2,1,3,4,7,9,5,6}
# s.remove(6)
# print(s)

'''
union
intersection
difference
issubset
issuperset
'''
'''union'''
# set1={1,2,3}
# set2={4,5,6}
# print(set1.union(set2))

'''intersection'''

# set1={1,2,3,4}
# set2={4,5,6}
# print(set1.intersection(set2))

'''differrence'''

# set1={1,2,3}
# set2={4,5,6}
# print(set1.difference(set2))

'''issuperset & issubset'''

# set1={1,2,3,4,5,6}
# set2={4,5,6}
# print(set1.issuperset(set2))
# print(set2.issubset(set1))

'''by using for loop'''

set1={1,2,3,4}
set2={4,5,6}
for i in {1,2,3,4}:
    print(i)
