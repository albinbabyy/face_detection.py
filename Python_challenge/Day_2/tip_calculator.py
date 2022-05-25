print("Welcome to Tip Calculator")

total_bill = float(input("What was the total bill? : "))

tip_percentage = int(input("What percentage tip would you like to give? 10,12 or 15? : "))

people = int(input("How many people to split the bill? : "))

bill_with_tip = total_bill * ((100 + tip_percentage) / 100)

bill_per_person = round(bill_with_tip / people , 2)

print(f"Each person should pay : {bill_per_person}")
