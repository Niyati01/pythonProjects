# Calculates the BMI and tells us if we are underweight overweight or normal.

height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))


bmi = weight/(height ** 2)
print(round(bmi,2))

if bmi < 18.5:
    print("Underweight")
elif(bmi < 25):
    print("Normal weight")
elif(bmi < 30):
    print("Overweight")
elif(bmi < 35):
    print("Obese")
elif bmi >= 35:
    print("Clinically Obese")

