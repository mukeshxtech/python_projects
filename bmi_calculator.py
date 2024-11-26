""" BMI calculator"""

height = float(input("What is your height ?\n"))
height = height*0.3048
weight = float(input("What is your weight ?\n"))
bmi = weight/(height**2)

if bmi < 18.5:
    print(f"BMI: {round(bmi,2)} and Category: Underweight")
elif 18.5 <= bmi <= 24.9:
    print(f"BMI: {round(bmi,2)} and Category: Normal")
elif 25.0 <= bmi <= 29.9:
    print(f"BMI: {round(bmi,2)} and Category: Overweight")
elif bmi >= 30:
    print(f"BMI: {round(bmi,2)} and Category: Obesity")
