t = (1,2,3)
print t

print t[-1]
print t[::-1]
print t.index(1)
print t[1]

num = (3,2,151,1239,435345)
# num[1] = 123 #cannot mutate, tuples are immutable
print num
print num.count(2) # count the value occured in the tuple
print num.index(151) # get the index of value
