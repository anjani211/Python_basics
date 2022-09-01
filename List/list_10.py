from itertools import count


# find sum and average in a list
ls = [2,3,4,5,4,3]

sum = 0

for i in ls:
    sum+=i

avg = sum/len(ls)
print(avg)
print(sum)