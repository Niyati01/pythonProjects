def prime_checker(number):
    is_prime = True
    if number <= 1:
        print("Number should be greater than 1")
    
    for n in range(2,number):
        if number % n == 0:
            is_prime = False
            #print(f"{number} is Prime.")
    
    if is_prime == True:
        print(f"{number} is Prime.")
    else:
        print(f"{number} is not a Prime.")

n = int(input("Check the number if its prime or not : "))
prime_checker(number = n)