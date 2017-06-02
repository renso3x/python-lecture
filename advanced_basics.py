#dictionaries

l = {'k1': 1, 'k2': 3}

print 'Dict items'
for k in l.iteritems():
	print k

print 'Dict values'
for v in l.itervalues():
	print v

print 'Dict keys'
for k in l.iterkeys():
	print k

#generating a dict that is a for loop
# x is the iteration of the loop
#comprehension
l = {x: x** 2 for x in range(0, 10)}
print l


#Advanced Lists
num = [1, 2, 3, 4]
#append inserts in the list while you pass a list value it will be a list also when append
#[1, 2, 3, 4, [5, 6]]
num.append([5, 6])
print num
#extend append in the list
#[1, 2, 3, 4, 5, 6]
num.extend([5, 6])
print num

print num.index(3)

num.pop()
print num
# get the element poped
popeed = num.pop()
print popeed

num.remove(1)
print num

#remove elements via value
num.remove(3)
print num

#NUMBERS

print hex(245) #hex
print bin(123) #binary
print pow(2, 3) # n to the power of x
print abs(-1000) #get the absolute value
print round(3) # returns a float
print round(3.1415926535, 2) #2nd arg is the decimal place


#Strings
s = 'hello world'
print s.capitalize()

print s.count('o')
print s.find('w')

alpha_str = 'r a n ge 2 0'
print alpha_str.isalnum() #alphanumeric
print alpha_str.isalpha() # if all alphabetic
print alpha_str.islower()
print alpha_str.isspace()
print alpha_str.isupper()
print alpha_str.endswith('0')
print alpha_str.endswith('e')


#Sets

s = set()

s.add(1)
s.add(2)
print s
sc = s.copy()
print sc

sc.add(3)
print s
print sc

print s.difference_update(sc)


s1 = {1, 2, 3}
s2 = {3, 2, 5, 4}

print s1.intersection(s2)
