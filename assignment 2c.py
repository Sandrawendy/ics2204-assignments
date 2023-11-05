#Sandra Wendy Katheu Kyavoa
#sct211-0047/2022
def calculate_bmi(weight_kg, height_m):
    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 24.9:
        return "normal weight"
    else:
        return "overweight"

# Get user input for weight and height
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight_kg, height_m)

# Interpret BMI and provide feedback
bmi_category = interpret_bmi(bmi)

print(f"Your BMI is: {bmi:.2f}")
print(f"You are classified as {bmi_category}.")

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Get user input for the year
year = int(input("Enter a year: "))

# Check if it's a leap year and provide the result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
