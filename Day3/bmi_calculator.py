# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round(weight / height ** 2)
UNDER_WEIGHT = 18.5
NORMAL_WEIGHT = 25
OVER_WEIGHT = 30
CLINICALLY_OBSE = 35
print("bmi ", bmi)
if (bmi <= UNDER_WEIGHT):
    print(f"Your BMI is {bmi}, You are underweight.")
elif (bmi > UNDER_WEIGHT and bmi < NORMAL_WEIGHT):
    print(f"Your BMI is {bmi}, You have a normal weight.")
elif (bmi > NORMAL_WEIGHT and bmi < OVER_WEIGHT):
    print(f"Your BMI is {bmi}, You are a overweight.")
elif (bmi > CLINICALLY_OBSE):
    print(f"Your BMI is {bmi}, You are obese.")
