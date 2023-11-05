#Sandra Wendy Katheu Kyavoa
#SCT211-0047/2022
import math

# Function to calculate the tip and split the bill
def calculate_tip_and_split_bill(total_bill, tip_percentage, num_people):
    # Convert the tip percentage to a decimal
    tip_decimal = tip_percentage / 100
    
    # Calculate the tip amount
    tip_amount = total_bill * tip_decimal
    
    # Calculate the total amount to be paid
    total_amount = total_bill + tip_amount
    
    # Calculate the amount each person should pay
    amount_per_person = total_amount / num_people
    
    return amount_per_person

# Input the total bill amount
total_bill = float(input("Enter the total bill amount: Ksh"))
4500        

# Input the tip percentage

tip_percentage = float(input("Enter the tip percentage (10, 12, or 15): "))
        
# Input the number of people

num_people = int(input("Enter the number of people: "))
        
# Calculate the amount each person should pay
amount_per_person = calculate_tip_and_split_bill(total_bill, tip_percentage, num_people)

# Display the result rounded to two decimal places
print(f"Each person should pay: Ksh{round(amount_per_person, 2)}")
