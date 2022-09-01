# program to swap two elements in a list

def swapElements(n,a,b):
    get = n[a],n[b]
    n[b],n[a]= get
    return n


n = [2,3,4,5,6,7,8,9]
a=2
b=3

print(swapElements(n,a,b))