#Advanced Numbers
print hex(1024)
print round(5.232222, 2)
#Advanced Strins
s = 'hello how are you Mary, are you feeling okay?'
def str_is_lower(s):
	checker = []
	for spl in s.split():
		for x in spl:
			if x.islower():
				checker.append({ x: x.islower() })


	print checker

str_is_lower(s)

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
def count_str(str, find):
	print str.count(find)

count_str(s, 'w')


#Advanced Sets
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

print set1.difference(set2)
print set1.union(set2)


#Advanced Dict
d = {k: x**3 for k,x in zip([0, 1, 2, 3, 4], range(5))}
print d

#Advanced List
l = [1,2,3,4]
l.reverse()
print l
print l[::]

l = [3,4,2,5,1]
l.sort()
print l
