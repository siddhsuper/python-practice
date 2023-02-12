# Write your code below this line 👇
# User Input
age = int(input("What is your current age?"))

# Contant Declaration
DAYS_YEAR = 365
WEEKS_YEAR = 52
MONTHS_YEAR = 12
MAX_AGE = 90

years_left = MAX_AGE - age

days = (MAX_AGE * DAYS_YEAR) - (DAYS_YEAR * age)
weeks = (MAX_AGE * WEEKS_YEAR) - (WEEKS_YEAR * age)
months = (MAX_AGE * MONTHS_YEAR) - (MONTHS_YEAR * age)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# Another way to calculate
days_left = years_left * DAYS_YEAR
weeks_left = years_left * WEEKS_YEAR
months_left = years_left * MONTHS_YEAR
print(
    f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
)
