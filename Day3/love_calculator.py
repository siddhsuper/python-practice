# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
first_name = input("What is your name? \n")
second_name = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
LOVE_CODE = "true"
LOVE_CODE_2 = "love"
tens_count = 0
for l in LOVE_CODE:
    tens_count += first_name.lower().count(l)
    tens_count += second_name.lower().count(l)
    print(tens_count)

tens_count *= 10
ones_count = 0
for c in LOVE_CODE_2:
    ones_count += first_name.lower().count(c)
    ones_count += second_name.lower().count(c)
    print(ones_count)

final_score = tens_count + ones_count
if final_score < 10 or final_score > 90:
    print(
        f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score > 40 and final_score < 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}")
