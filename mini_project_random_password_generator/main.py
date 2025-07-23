import random

class Game:

    game_list = ["r", "p", "s"]

    def __init__(self):
        self.user_points = 0
        self.computer_points = 0

    def play(self):
        user_choice = input("Rock, paper or scissors [r/p/s]? ")
        user_index = self.game_list.index(user_choice)
        computer_index = random.randint(0, 2)
        computer_choice = self.game_list[computer_index]
        print(f"You: {user_choice} | Computer: {computer_choice}")
        message = self.compare(user_index, computer_index)
        print(message)

    def compare(self, user_choice, computer_choice):
        # r = 0
        # p = 1
        # s = 2
        if (user_choice > computer_choice or computer_choice - user_choice == 2) and not (user_choice - computer_choice == 2):
            self.user_points += 1
            return "You won this round!"
        elif user_choice == computer_choice:
            return "This round is a tie."
        else:
            self.computer_points += 1
            return "You lost this round!"

    def summary(self):
        print(f"[Game summary] Your points: {self.user_points} | Computer points: {self.computer_points}")
        if self.user_points > self.computer_points:
            print("You won.")
        elif self.user_points == self.computer_points:
            print("It was a tie.")
        else:
            print("Computer won.")


print("--- Rock Paper Scissors Game ---")
yes = True
while yes:
    try:
        number_of_rounds = int(input("How many rounds would you like to play? "))
        yes = False
    except:
        print("Invalid input, enter a real whole number.")

game = Game()

for i in range(number_of_rounds):
    game.play()

game.summary()



