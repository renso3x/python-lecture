temp = [0, 22, 5, 40, 199]

#map
farenheit = lambda T: (9.0/5)*T + 32
res = map(farenheit, temp)
print res
print map(lambda x: x* -1, temp)


#reduce
print reduce(lambda x,y: x+y, temp)
print reduce(lambda x,y: x if x > y else y, temp)

#filter
print filter(lambda x: x % 2 == 0, temp)
print filter(lambda num: num > 3, temp)

#zip
a = [1, 2, 3]
b = [4, 5, 6]
print zip(a, b)

#enumarate
l = ['a', 'b','c']
for (k, v) in enumerate(l):
	print k, v

#all and any
#if all are true in iterables then returns true
# any if iterables has true then returns True
l = [True, True, False, False]
print all(l)

#complex
print complex(2, 3)
