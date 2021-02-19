# Selection Sort

num_list = [2,4,1,3,5]

num_length = int(len(num_list))

for i in range(0,num_length-2):

    for j in range(i+1,num_length-1):
        
        if num_list[j] < num_list[i]:
            print(f"i={i} j={j} numlist = {num_list}")
            num_list[i],num_list[j] = num_list[j],num_list[i]
            print(f"i={i} j={j} numlist = {num_list}")
            print("")
            


print(f"Sorted List : {num_list}")
