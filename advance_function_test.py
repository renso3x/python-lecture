def word_lengths(l):
	wrd = l.split()
	print map(lambda s: len(s), wrd)

word_lengths('How long are the words in this phrase')

def digits_to_num(digits):
	print reduce(lambda x,y: x*10 + y,  digits)

digits_to_num([3, 4, 3, 2, 1])


def filter_words(word_list, letter):
	print filter(lambda s: s[0] == letter, word_list)

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_words(l, 'h')

def concatenate(l1, l2, connector):
	concat = []
	for l in zip(l1, l2):
		concat.append(l[0] + connector + l[1])
	print concat

concatenate(['A', 'B'], ['a', 'b'], '-')

def d_list(L):
	dic = {}
	for k, l in enumerate(L):
		dic[l] = k
	print dic

d_list(['a', 'b', 'c'])

def count_match_index(L):
	matched = []
	for k, v in enumerate(L):
		if k == v:
			matched.append(v)

	print len(matched)

count_match_index([0, 2, 2, 1, 5, 5, 6, 10])
