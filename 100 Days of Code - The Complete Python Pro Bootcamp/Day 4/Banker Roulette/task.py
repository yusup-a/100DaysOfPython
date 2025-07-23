import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(friends[random.randint(0, len(friends)-1)]) #1st option more technical
print(random.choice(friends)) #2nd option more simple