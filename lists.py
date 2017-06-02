from __future__ import print_function
my_list = ['string', 1, 23, 'o']
print(my_list)
print('Length of the list {x}'.format(x = len(my_list)))
print('Grabbing the first element {x}'.format(x = my_list[:1]))
concat = 'Hello World'
my_list = my_list + [concat] # concat or adding to lists
print(my_list)
l = [1, 2, 3]
l.append(4)
print(l)
l.append('this is an append')
print(l)
third = l.pop(3)
print(l)
print(third)
new_list = ['a', 'f', 'z', 'k', 'h']
new_list.reverse()
print(new_list)
new_list.sort()
print(new_list)

#Nested Lists
l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
l_3 = [7, 8, 9]
matrix = [l_1, l_2, l_3]
print(matrix)
print(matrix[0]) #return first element of the matrix
print(matrix[0][1]) #return first element of the index
print(matrix[1][1]) #return first element of the index
print(matrix[2][0]) #return first element of the index

first_col = [row[0] for row in matrix]
print(first_col)
