l = [1,2,3,4,5]
list_sum = 0
for num in l:
	list_sum += num
	if num % 2 == 0:
		print 'here are even numbers %s' % num
	else:
		print 'odd number'

print 'Total sum: %s' % list_sum

s = 'this is a string'
for item in s:
	if item != ' ':
		print item

#tuple
tup = (1,2,3,4,5)
for t in tup:
	print t
l = [(2, 4), (6, 8), (10, 12)]
for tup in l:
	print tup

for (t1, t2) in l: #unpacking the tuple
	print t1

#dictionary
d = {'k1': 1, 'k2': 2, 'k3': 3}
for i, v in d.iteritems():
	print v
