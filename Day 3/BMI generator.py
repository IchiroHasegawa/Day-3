print("BMI Calculator")
height_cm = float(input("What is your height in centimeters? "))
height = height_cm / 100
weight = float(input("What is your weight in kilograms? "))
BMI = weight / (height ** 2)
print(f"Your BMI is {round(BMI, 2)}")
if BMI < 18.5:
    print("you are underweight")
elif BMI <24.9:
    print("you are normal")
else:
    print("you are overweight")