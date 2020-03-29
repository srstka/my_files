height = float(input("To calculate your BMI please enter your hight in meters: "))
weight = float(input("and weight in kg: "))

bmi = round(weight/(height*height),1)

if bmi <=18.5:
    print("You are Underweight, your BMI index is:",bmi)
elif bmi >18.5 and bmi<=24.9:
    print("You have Normal weight, your BMI index is:",bmi)
elif bmi >24.9 and bmi<=29.9:
    print("You are Overweight, your BMI index is:",bmi)
else:
    print("You have Obesity, your BMI index is:",bmi)
