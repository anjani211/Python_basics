# frequency of elements in string
st = input()
p= {}
for i in st:
    if i in p:
        p[i] +=1
    else:
        p[i] = 1
print(p)