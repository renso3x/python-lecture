f = open('text.txt')
print f.read()
print f.seek(0) #go back to the first line
print f.read()

print f.readlines()

for line in f:
	print line
