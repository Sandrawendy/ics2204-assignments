class BillSplitter:
    def __init__(self, total_bill, tip_percentage, num_people):
        self.total_bill = total_bill
        self.tip_percentage = tip_percentage
        self.num_people = num_people

    def calculate_tip_amount(self):
        tip_decimal = self.tip_percentage / 100
        return self.total_bill * tip_decimal

    def calculate_total_bill(self):
        tip_amount = self.calculate_tip_amount()
        return self.total_bill + tip_amount

    def calculate_amount_per_person(self):
        total_amount = self.calculate_total_bill()
        return total_amount / self.num_people

    def display_amount_per_person(self):
        amount_per_person = self.calculate_amount_per_person()
        print(f"Each person should pay: Ksh{round(amount_per_person, 2)}")


# Taking input and using the BillSplitter class
total_bill = float(input("Enter the total bill amount: Ksh "))
tip_percentage = float(input("Enter the tip percentage (10, 12, or 15): "))
num_people = int(input("Enter the number of people: "))

# Creating an instance of BillSplitter
bill_splitter = BillSplitter(total_bill, tip_percentage, num_people)
bill_splitter.display_amount_per_person()
