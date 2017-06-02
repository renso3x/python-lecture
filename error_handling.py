try:
	2 + 'e'
except:
	print 'An error occured'
finally:
	print 'finally'


try:
	f = open('text.txt', 'w')
	f.write('Test write')
except:
	print 'No file found.'
else:
	print 'File write success'

def askInt():
	while True:
		try:
			val = int(input('Please enter an integer: '))
		except:
			print 'Not an integer'
			continue #continue on asking
		else:
			print 'That is an integer'
			break
		finally:
			print 'Finally block'

	print val
# askInt()

#homework
try:
	for i in ['a', 'b', 'c']:
		print i ** 2
except:
	print 'This are not numeric variables'

x = 5
y = 0

try:
	z = x / y
except:
	print 'Not a number'
finally:
	print 'All Done'

def ask():
	while True:
		try:
			val = int(input('Input an integer: '))
		except:
			print 'An error occured! Please try again!'
			continue
		else:
			break

	print 'Thank you, your number squared is: ', val**2

ask()
