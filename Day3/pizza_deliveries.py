# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
SMALL_PIZZA = 15
MEDIUM_PIZZA = 20
LARGE_PIZZA = 25

PEPPERONI_SMALL = 2
PEPPERONI_BIG = 3

EXTRA_CHEESE = 1

if size == "S":
    bill = SMALL_PIZZA
    if (add_pepperoni == "Y" and extra_cheese == "Y"):
        bill += PEPPERONI_SMALL
        bill += EXTRA_CHEESE
    elif (add_pepperoni == "Y"):
        bill += PEPPERONI_SMALL
    elif extra_cheese == "Y":
        bill += EXTRA_CHEESE
elif size == "M":
    bill = MEDIUM_PIZZA
    if (add_pepperoni == "Y" and extra_cheese == "Y"):
        bill += PEPPERONI_BIG
        bill += EXTRA_CHEESE
    elif (add_pepperoni == "Y"):
        bill += PEPPERONI_BIG
    elif extra_cheese == "Y":
        bill += EXTRA_CHEESE
elif size == "L":
    bill = LARGE_PIZZA
    if (add_pepperoni == "Y" and extra_cheese == "Y"):
        bill += PEPPERONI_BIG
        bill += EXTRA_CHEESE
    elif (add_pepperoni == "Y"):
        bill += PEPPERONI_BIG
    elif extra_cheese == "Y":
        bill += EXTRA_CHEESE

print(f"Your final bill is: ${bill}")
