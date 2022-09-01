# swap elements in a string list python

ls = ['manish', 'is','a','good','boy']

b = [i.replace('m','h').replace('g','d').replace('b','y').replace('y','b') for i in ls]
print(b)
