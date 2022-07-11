import random
for i in range(4):
    print(random.random())
    print(random.randint(10,20))

members = ['John', "jane", "peter", "Bob"]
leader=(random.choice(members))
print(leader)

# dice exercise

x = random.randint(1, 4)

y = random.randint(1, 4)
print(f"({x},{y})")



class Dice:
    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return (x, y)


_roll = Dice()
_roll.roll()




