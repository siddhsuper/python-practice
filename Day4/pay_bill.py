import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
random_number = random.randint(1, len(names)-1)
print(f"person going to pay the bill is {names[random_number]}")
