from __future__ import print_function

my_dict = {'key1' : 'value', 'key2': 'value2', 'k3': '3.5', 'k4': 3.5}
print(my_dict)
print(my_dict['key1'])

my_dict['k4'] += 30;
print(my_dict['k4'])


new_dict = {}
new_dict['a'] = 'A'
new_dict['b'] = 'B'
new_dict['c'] = 'C'
print(new_dict)


profile = {
	"name": "Romeo Enso",
	"age": 23,
	"hobbies": [
		"art",
		"programming",
		"bug fixing"
	],
}

print(profile)
print(profile["name"])
print(profile["age"])
print(profile["hobbies"])
print(profile["hobbies"][1])
print(profile.keys())
print(profile.items())
