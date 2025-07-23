import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

userInp = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while userInp == "y":
    print("\n"*20)
    print(art.logo)
    myCards = []
    compCards = []

    myCards.append(random.choice(cards))
    myCards.append(random.choice(cards))
    compCards.append(random.choice(cards))
    compCards.append(random.choice(cards))

    myScore = sum(myCards)
    compScore = sum(compCards)

    if myScore == 21 and len(myCards) == 2:
        myScore = 0

    if compScore == 21 and len(compCards) == 2:
        compScore = 0

    print(f"\t Your cards: {myCards}, current score: {myScore}")
    print(f"\t Computer's first card: {compCards[0]}")

    if myScore != 0:
        userInp2 = input("Type 'y' to get another card, type 'n' to pass: ")

    while userInp2 == 'y':
        myCards.append(random.choice(cards))
        myScore = sum(myCards)

        if myScore > 21:
            if 11 in myCards:
                myCards.remove(11)
                myCards.append(1)
                myScore = sum(myCards)
            else:
                break

        print(f"\t Your cards: {myCards}, current score: {myScore}")
        print(f"\t Computer's first card: {compCards[0]}")

        if myScore > 21:
            break
        userInp2 = input("Type 'y' to get another card, type 'n' to pass: ")

    if myScore <= 21:
        if myScore != 0:
            while compScore < 17:
                compCards.append(random.choice(cards))
                compScore = sum(compCards)
                if compScore > 21:
                    if 11 in compCards:
                        compCards.remove(11)
                        compCards.append(1)
                        compScore = sum(compCards)


        if compScore == 21 and len(compCards) == 2:
            compScore = 0

    print(f"\tYour final hand: {myCards}, final score: {myScore}")
    print(f"\tComputer's final hand: {compCards}, final score: {compScore}")

    if myScore > 21:
        print("You went over. You lose \U0001F62D")
    elif compScore > 21:
        print("Opponent went over. You win \U0001F601")
    elif compScore == myScore:
        print("Draw \U0001F643")
    elif myScore == 0:
        print("Win with a Blackjack \U0001F60E")
    elif compScore == 0:
        print("Lose, opponent has Blackjack \U0001F628")
    elif compScore > myScore:
        print("You lose \U0001F624")
    else:
        print("You win \U0001F603")

    userInp = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
