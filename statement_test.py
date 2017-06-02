st = 'Print only the words that start with s in this sentence'
split = st.split()

for s in split:
	if s[0] == 's':
		print s

print range(0, 10, 2)

#divisible by 3
ls = [x for x in range(10) if x % 3 == 0]
print ls


st = 'Print every word in this sentence that has an even number of letters'
st_split = st.split()

for s in st_split:
	if len(s) % 2 == 0:
		print s + '===> even'

#fizzBuzz
r = range(1, 100)
for i in r:
	if i % 3 == 0:
		print '%s Fizz' % i
	elif i % 5 == 0:
		print '%s Buzz' % i
	elif i % 5 == 0 and i % 3 == 0:
		print '%s FizzBuzz' % i
	else:
		print i

stre = 'Create a list of the first letters of every word in this string'
stre_split = stre.split()

new_st = [st[0] for st in stre_split]
print new_st
