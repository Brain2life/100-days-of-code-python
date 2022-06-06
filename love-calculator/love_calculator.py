# https://app.codingrooms.com/w/jG2Aj97tbRef

# Example input:
# name1 = "Kanye West"
# name2 = "Kim Kardashian"
# Your score is 42, you are alright together.

# 🚨 Don't change the code below 👇
from itertools import count


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()

t_letter_total = name1_lower.count("t") + name2_lower.count("t")
r_letter_total = name1_lower.count("r") + name2_lower.count("r")
u_letter_total = name1_lower.count("u") + name2_lower.count("u")
e_letter_total = name1_lower.count("e") + name2_lower.count("e")
l_letter_total = name1_lower.count("l") + name2_lower.count("l")
o_letter_total = name1_lower.count("o") + name2_lower.count("o")
v_letter_total = name1_lower.count("v") + name2_lower.count("v")

true_word_total = t_letter_total + r_letter_total + u_letter_total + e_letter_total
love_word_total = l_letter_total + o_letter_total + v_letter_total + e_letter_total

final_score = str(true_word_total) + str(love_word_total)

if int(final_score) < 10 or int(final_score) > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif int(final_score) > 40 and int(final_score) < 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")