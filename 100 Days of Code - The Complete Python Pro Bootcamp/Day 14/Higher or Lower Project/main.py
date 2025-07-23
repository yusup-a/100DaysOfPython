from game_data import data
import art
import random

def compare(a, b):
    followerA = a["follower_count"]
    followerB = b["follower_count"]

    if followerA > followerB:
        return "A"
    else:
        return "B"

score = 0
gameOver = False
personB = random.choice(data)

while not gameOver:
    print(art.logo)

    if score != 0:
        print(f"You're right! Current score: {score}.")

    personA = personB
    personB = random.choice(data)

    while personB == personA:
        personB = random.choice(data)

    print(f"Compare A: {personA["name"]},", end='')
    print(f"a {personA["description"]},", end='')
    print(f"from {personA["country"]}.")

    print(art.vs)
    print(f"Against B: {personB["name"]},", end='')
    print(f"a {personB["description"]},", end='')
    print(f"from {personB["country"]}.")

    userInp = input("Who has more followers? Type 'A' or 'B': ").upper()

    if userInp == compare(personA, personB):
        score += 1
    else:
        gameOver = True

print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")