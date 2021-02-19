# Bubble Sort

#num_list = [2,4,1,3,5]

#num_list = [64, 34, 25, 12, 22, 11, 90]
num_list = [5,4,3,2,1]
num_len = int(len(num_list))

for j in range(1,num_len-1):
    for i in range(0,num_len-1):
        if num_list[i] > num_list[i+1]:
            num_list[i],num_list[i+1] = num_list[i+1],num_list[i]
            print(f"j = {j}, i = {i} , numlist = {num_list}")
        else:
            print(f"j = {j}, i = {i} , numlist = {num_list}")


print(num_list)