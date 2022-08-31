# python program to interchange first and last elements in a list
ls = [1,2,3,2,1,3,4,6]
def swaplst(n):
    s = len(n)
    temp = n[0]
    n[0] = n[s-1]
    n[s-1] = temp
    return n


print(swaplst(ls))