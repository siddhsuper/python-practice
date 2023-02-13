# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Year {year} is a leap year")
        else:
            print(f"Year !400! {year} is not a leap year")
    else:
        print(f"Year !100! {year} is a leap year")
else:
    print(f"Year {year} is not a leap year")
