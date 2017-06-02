def name_of_function(arg1, arg2):
	pass

name_of_function(0, 1)

def addition(arg1, arg2):
	print arg1 + arg2

addition(5, 10)

def say_hello(name):
	print 'Hello %s' % name

say_hello('Romeo')
say_hello('Raymund')


def subtract(arg1, arg2):
	return arg1 - arg2

x = subtract(10, 4)
print x


def is_prime(num):
	for n in range(2, num):
		if num % n == 0:
			print 'Not a prime!'
			break
	else:
		print 'The number is prime!'

is_prime(10)
is_prime(13)
is_prime(12)
