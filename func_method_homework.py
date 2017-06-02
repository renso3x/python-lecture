def vol(rad):
	# (4/3) * ((3.14) * (rad**3))
	return (4/float(3.0)) * (3.14 * (rad**3))

print vol(1)

def ran_check(num, low, high):
	for x in range(low, high):
		if x == num:
			return True

print ran_check(3, 1, 10) #true
print ran_check(11, 1, 10) #none


def up_low(s):
	upper_str = []
	lower_str = []

	for char in s:
		if char == char.isupper() and char != ' ' and char != ',' and char != '.' and char != '?':
			upper_str.append(char)
		elif char == char.lower():
			lower_str.append(char)

	print 'No. of Upper case characters: %s' % len(upper_str)
	print 'No. of Lower case characters: %s' % len(lower_str)

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')

list = [1,1,1,1,2,2,3,3,3,3,4,5]

def unique_list(l):
	# return set(l)
	x = []
	for a in l:
		if a not in x:
			x.append(a)

	return x

print unique_list(list)


def multiplier(args):
	total = 1
	for num in args:
		total *= num

	print total

multiplier([1, 2, 3, -4])


def palindrome(s):
	rev = s[::-1]#reverse a string
	if rev == s:
		return True

print palindrome('helleh')
print palindrome('state')
print palindrome('hello')
print palindrome('madam')
print palindrome('nurses')

def ispangram(str1):
	str1 = str1.split(' ');
	alpha = []

	for characters in str1:
		for char in characters:
			alpha.append(char.lower())

	return set(alpha)

print ispangram("The quick brown fox jumps over the lazy dog")
