def square(num):
	return num**2

print square(4)

def squares(num): return num**2

print squares(4)

x = lambda num: num**2

print x(3)

is_even = lambda num: num % 2 == 0

print is_even(1)
print is_even(2)
print is_even(3)

first = lambda s: s[0]

print first('hello')

reverse = lambda s: s[::-1]

print reverse('romeo')

adder = lambda x, y: x + y

print adder(10, 12)
