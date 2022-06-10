# https://replit.com/@appbrewery/rock-paper-scissors-start

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

available_options = [rock, paper, scissors]

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
if human_choice >=3 or human_choice < 0:
    print("You typed an invalid number, you lost!")
    exit()
else:
    human_choice = available_options[human_choice]

computer_choice = random.choice(available_options)

print("Human chose: \n", human_choice)
print("Computer chose: \n", computer_choice)

if human_choice == computer_choice:
    print("It's draw. Try again")
elif human_choice == paper and computer_choice == rock:
    print("You won")
elif human_choice == scissors and computer_choice == paper:
    print("You won")
elif human_choice == rock and computer_choice == scissors:
    print("You won")
else:
    print("You lose")