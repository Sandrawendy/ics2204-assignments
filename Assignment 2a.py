#sandra wendy katheu kyavoa
#SCT211-0047/2022
def greet_and_add():
    # Ask for the user's name
    name = input("Please enter your name: ")
    print(f"Hello, {name}!")

    # Ask for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Add the numbers
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")

# Call the function to run it
greet_and_add()
from datetime import datetime

def calculate_age():
    # Ask for the user's birth year
    birth_year = int(input("Please enter your birth year (e.g., 1990): "))

    # Get the current date
    current_date = datetime.now()

    # Calculate the age
    age = current_date.year - birth_year

    # Calculate the number of months and days
    birth_month = int(input("Please enter your birth month (e.g., 1-12): "))
    birth_day = int(input("Please enter your birth day (e.g., 1-31): "))

    if current_date.month < birth_month or (current_date.month == birth_month and current_date.day < birth_day):
        age -= 1  # Subtract 1 year if the birthday hasn't occurred yet this year

    # Calculate the remaining months and days
    if current_date.month < birth_month:
        months = 12 - (birth_month - current_date.month)
    else:
        months = current_date.month - birth_month

    if current_date.day < birth_day:
        days = birth_day - current_date.day
        if months > 0:
            months -= 1
    else:
        days = current_date.day - birth_day

    print(f"You are {age} years, {months} months, and {days} days old.")

# Call the function to run it
calculate_age()
