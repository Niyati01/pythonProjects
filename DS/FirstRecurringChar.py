#First recurring character
arry = [4,1,2,4,5,7,2,4]

dict1 = {}

for i in arry:           #O(n)
    if i in dict1:
        dict1[i] += 1
        print(i)
        break
    else:
        dict1[i] = 0

