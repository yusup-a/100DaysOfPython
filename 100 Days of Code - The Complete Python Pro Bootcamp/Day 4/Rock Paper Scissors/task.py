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

userInput = int(input("What do you chose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

computerChoice = random.randint(0,2)

if userInput == 0:
    print(rock)
    if computerChoice == 0:
        print("Computer chose:\n" + rock + "\nIt is a draw")
    elif computerChoice == 1:
        print("Computer chose:\n" + paper + "\nYou lose")
    elif computerChoice == 2:
        print("Computer chose:\n" + scissors + "\nYou win")
elif userInput == 1:
    print(paper)
    if computerChoice == 0:
        print("Computer chose:\n" + rock + "\nYou win")
    elif computerChoice == 1:
        print("Computer chose:\n" + paper + "\nIt is a draw")
    elif computerChoice == 2:
        print("Computer chose:\n" + scissors + "\nYou lose")
elif userInput == 2:
    print(scissors)
    if computerChoice == 0:
        print("Computer chose:\n" + rock + "\nYou lose")
    elif computerChoice == 1:
        print("Computer chose:\n" + paper + "\nYou win")
    elif computerChoice == 2:
        print("Computer chose:\n" + scissors + "\nIt is a draw")
