# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)

bid_dictionary = {}

name = input("What is your name?: ")
bid = int(input("What is your bid?: $"))
bid_dictionary[name] = bid
strAnswer = input("Are there any other bidders? Type 'yes' or 'no'. ")

while strAnswer == "yes":
    print("\n" * 20)
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_dictionary[name] = bid
    strAnswer = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

maxVal = 0
maxName = ""
for name in bid_dictionary:
    if bid_dictionary[name] > maxVal:
        maxVal = bid_dictionary[name]
        maxName = name

print(f"The winner is {maxName} with a bid of ${maxVal}.")