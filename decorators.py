s = 'Hello world'
# print globals() - call all the dictionary with the global variables
# print locals()

def hello(name = "ROMEO"):
	return "Hello " + name

greet = hello #assign function to a variable

print greet()
del hello #delete a object or a funciton
print greet() # still works even hello is deleted

#function within functions
def hello(name= 'Romeo'):
	def greet():
		return "\t Inside the greet function"
	def welcome():
		return "\t Inside the welcome function"

	if name == 'Romeo':
		#returns only the function calling without parens
		#if function() it will be executed
		return greet
	else:
		return welcome

x = hello(name = 'Jose')
print x()


#function as arguments
def hello():
	return "Hi Jose!"

#pass a function
def other(func):
	print "other code goes here"
	#execute a function
	print func()

other(hello)


def new_decorator(func):
	def wrap_func():
		print "Code here, before executing the function"
		func()
		print "Code here will execute after the function"

	return wrap_func

def func_needs_decorator():
	print "This function needs a decorator"

#manually assigning the decorator
func_needs_new_dec = new_decorator(func_needs_decorator)

func_needs_new_dec()

#automatic call a func inside a decorator
@new_decorator
def func_needs_decorator():
	print "This function needs a decorator"

func_needs_decorator()
