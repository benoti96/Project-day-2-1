#Tip Calculator
print("Welcome to Oti's Tip Calculator!")

total_bill = float(input("1st Question: What was the total bill? £"))


tip = int(input("2nd Question: What percentage tip would you like to give? 10,12 or 15? "))

number_of_people = int(input("3rd Question: How many people are going to split the bill? "))
          
bill_with_tip = tip / 100 * total_bill + total_bill

bill_per_person = bill_with_tip / number_of_people

final_bill_amount = round(bill_per_person, 2)

print(f"Each person should pay £{final_bill_amount}")

