from collections import Counter, namedtuple

l = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]

print Counter(l)

print Counter('aabsbsbsbhshhbbsbs')

s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

print Counter(words)

print sum(Counter(words).values()) # sum up the collections
print list(Counter(words))# display all values
print set(Counter(words))
print dict(Counter(words))

#named tuples
Dog = namedtuple('Dog', 'name breed sound age')
bar = Dog(name = 'Bar', breed = 'askal', sound = 'roof!', age = 3)
print bar
