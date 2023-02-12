# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
bill_value = float(input("What's the bill ? \n"))
tip_value = int(input("Choose the tip you want to pay 10% 12% 15% ?\n"))
person = int(input("How many people you are splitting? "))
bill_value += bill_value * (tip_value/100)
each_bill = round(bill_value / person, 2)
# formatting the bill upto 2 decimal places
final_amount = "{:.2f}".format(each_bill)
print("Each person should pay: $", final_amount)
