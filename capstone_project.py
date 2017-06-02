from decimal import *
import math

#fibonnaci
def genfib(n):
	a = 1
	b = 1
	l = []

	for i in range(n):
		l.append(a)
		temp = a
		a, b= b, temp + b
	yield l

for x in genfib(10):
	print x


#find PI to the Nth Digit
def get_nth_of_pi(n):
	return round(math.pi, n)

print get_nth_of_pi(10)
print get_nth_of_pi(5)

def get_nth_of_e(n):
	return round(math.e, n)

print get_nth_of_e(30)
print get_nth_of_e(3)

#prime factor
def ifPrime():
	n = int(raw_input('Input a number to check if prime: '))
	if (n != 1) and (n / 1 == n) and (n % 2 != 0) and (n % 3 != 0) or (n / 2 == 1):
		print '%s is prime' % n
		ifPrime()
	else:
		print '%s is not prime' % n
		ifPrime()


ifPrime()
