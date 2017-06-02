# from __future__ import division
# print 2/3
print float(2)/3
print 'square root of 100 = %s' % (100**2) #square
print 'square root of 100 = %s' % (100**0.5) #square root

print 4 * (6 + 5) #44
print 4 * 6 + 5 #29
print 4 + 6 *5 #34

print 3 + 1.5 + 4

s = 'hello'
print s[1]
print s[::-1]
print s[-1]

l = [0,0]
add_l = 0
l.append(add_l)
print l

l = [1,2,[3,4,'hello']]
l[2][2] = 'goodbye'
print l

new_l = [6,4,5,5,6]
print sorted(new_l)
new_l.sort()
print new_l

d = {'simple_key':'hello'}
print d['simple_key']
d = {'k1':{'k2':'hello'}}
print d['k1']['k2']
d = {
	'k1':
		[
			{
				'nest_key': [
					'this is deep',
					['hello']
				]
			}
		]
	}
print d['k1'][0]['nest_key'][1]

d = {
	'k1':
	[
		1,
		2,
		{
			'k2': [
				'this is tricky',
				{
					'tough':[
						1,
						2,
						['hello']
					]
				}
			]
		}
	]
}
print d['k1'][2]['k2'][1]['tough'][2]
#cannot sort dictionaries because they are not sequensial these are mappings
#tuples
t = (1,2,3)

#set are unique elements stored inside
l = [1,2,2,33,4,4,11,22,3,3,2]
print set(l)

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

#True or False?
print (l_one[2][0] >= l_two[2]['k1']) #false
