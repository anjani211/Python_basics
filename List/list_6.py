# check if element is present in list

ls = [2,3,2,4,5,6,7,8,5,3,2,]
check = int(input('enter number'))
for i in ls:
    if check in ls:
        print("yes")
        break
    else:
        print('no')