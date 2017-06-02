import random
#
# def gencube(n):
# 	for i in range(n):
# 		yield i**3
#
# for x in gencube(10):
# 	print x
#
# def genfibon(n):
# 	a = 1
# 	b = 1
#
# 	for x in range(n):
# 		yield a
# 		temp = a
# 		a = b
# 		b = temp + b
#
# for i in genfibon(10):
# 	print i
#
# def simple_gen():
# 	for x in range(3):
# 		yield x
#
# g = simple_gen()
#
# print next(g)
# print next(g)
# print next(g)
#
# s = iter('hello')
# print next(s)
# print next(s)
# print next(s)
# print next(s)
# print next(s)

# def next_num():
# 	yield 1000
# 	yield 222
# 	yield 3333
#
# nex = next_num()
#
# print next(nex)
# print next(nex)
# print next(nex)

#homework
def gensquares(N):
	for i in range(N):
		yield i**2

for x in gensquares(10):
	print x

def rand_num(low, high, n):
	for i in range(n):
		yield random.randint(low, high)

for num in rand_num(1, 10, 12):
	print num

s = iter('hello')
print next(s)
print next(s)
print next(s)
print next(s)
print next(s)

""""
Generator is helpfull when you are creating a large list
of data. Yield is helpful because it tracks the value and you don't
need to trace it for yourself. Once a yield value is created
it will call next so that it will go get the next value.
"""

#generator comprehension
my_list = [1, 2, 3, 4, 5]

gencomp = (item for item in my_list if item > 3)

print gencomp.next()
print gencomp.next()
