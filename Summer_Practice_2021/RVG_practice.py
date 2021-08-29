import random

for i in range(3):
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Mosh', 'Bob']
leader = random.choice(members)
print(leader)

#Roll a Dice
a = random.randint(1, 6)