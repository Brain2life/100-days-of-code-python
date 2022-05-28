# https://replit.com/@appbrewery/tip-calculator-start

# Check inputs:
# Total bill: 124.56
# Percentage: 12
# Number of people: 7
# Output: $19.93

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

each_person_payment = round((total_bill / number_of_people) * (1 + percentage / 100), 2)
print(f"Each person should pay: ${each_person_payment}")