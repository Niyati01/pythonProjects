print("Welcome to Python pizza deliveries!")
size = input("What Size Pizza do you want? S, M, L : ")
add_pepperoni = input("Do you want Pepperoni? Y or N : ")
extra_Cheese = input("Do you want extra cheese? Y or N : ")


# Small pizza = $15
# Medium pizza = $20
# Large Pizza = $ 25

# Pepperoni
# Small +$2
# Medium or Large +$3

# Extra Cheese +$1

total = 0

if size == 'S':
    total += 15
elif size == 'M':
    total += 20
elif size == 'L':
    total += 25

if add_pepperoni == 'Y':
    if size == 'S':
        total += 2
    else:
        total += 3

if extra_Cheese == 'Y':
    total += 1

print(f"You orderered {size} pizza with {add_pepperoni} pepperoni and {extra_Cheese} extra Cheese. Total bill is ${total}.")