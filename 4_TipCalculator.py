print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10,12 or 15? "))
no_of_people = int(input("How many people ot split the bill?"))

bill_with_tip = (total_bill * tip_percent/100) + total_bill
bill_per_person = round(bill_with_tip/no_of_people,2)

print(f"Each person pays ${bill_per_person}")