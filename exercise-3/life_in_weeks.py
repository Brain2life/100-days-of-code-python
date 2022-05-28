# https://waitbutwhy.com/2014/05/life-weeks.html
# https://replit.com/@appbrewery/day-2-3-exercise?v=1

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
overall_days = 90 * 365
overall_weeks = 90 * 52
overall_months = 90 * 12

days_left = overall_days - (365 * int(age))
weeks_left = overall_weeks - (52 * int(age))
months_left = overall_months - (12 * int(age))

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")