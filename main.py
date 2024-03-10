import random
import sys

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
ascii_art_choices = [rock, paper, scissors]
ai_score = 0
user_score = 0

while True:
    ai_choice = random.randint(0, 2)
    user_choice = -1
    while user_choice not in ["0", "1", "2"]:
        user_choice = input("Enter 0 for rock, 1 for paper or 2 for scissors (type \"exit\" to exit the game). ")
        if user_choice == "exit":
            sys.exit(0)

    user_choice = int(user_choice)
    print(f"Computer choice: {ascii_art_choices[ai_choice]}")
    print(f"Your choice: {ascii_art_choices[user_choice]}")
    if ai_choice == 0:
        if user_choice == 0:
            print("Draw.")
        elif user_choice == 1:
            print("You won!")
            user_score += 1
        elif user_choice == 2:
            print("You lost.")
            ai_score += 1

    if ai_choice == 1:
        if user_choice == 0:
            print("You lost.")
            ai_score += 1
        elif user_choice == 1:
            print("Draw.")
        elif user_choice == 2:
            print("You won!")
            user_score += 1

    if ai_choice == 2:
        if user_choice == 0:
            print("You won!")
            user_score += 1
        elif user_choice == 1:
            print("You lost")
            ai_score += 1
        elif user_choice == 2:
            print("Draw.")
    print(f"score: AI {ai_score}-{user_score} Player")
