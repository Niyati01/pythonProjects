print("Welcome to Love Calculator!")
name1 = input("Enter the first name : ")
name2 = input("Enter the second name: ")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

true = t + r + u + e

love = l + o + v + e

love_score = str(true) + str(love)

print(f"Your love score is {love_score}")