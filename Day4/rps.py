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

# Write your code below this line 👇

image_list = [rock, paper, scissors]

user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if user_choice >= 3:
    print("Typed a invalid number, you loose")
else:
    print(f"You choose {image_list[user_choice]}")
    computer_choice = random.randrange(0, 2)
    print(f"Computer choose {image_list[computer_choice]}")
    if user_choice == computer_choice:
        print("sorry try again")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 2 and computer_choice == 0:
        print("You loose")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice > user_choice:
        print("You loose")
    else:
        print("invalid choice")
