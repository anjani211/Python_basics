# Sum of number digits in list
tl = [22,33,44,56,56,54,34]
res=[]
for i in  tl:
    sum = 0
    for digit in str(i):

        sum +=int(digit)
    res.append(sum)

print(res)
    