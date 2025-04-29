import random

def score(comp, user):
    if comp == user:
        return 0
    elif (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
        return -1  # user loses
    else:
        return 1   # user wins

options = ["Snake", "Water", "Gun"]

comp = random.randint(0, 2)
user = int(input("Enter 0 for Snake, 1 for Water, and 2 for Gun: "))

t1 = score(comp, user)

print(f"Computer chose {options[comp]}")
print(f"You chose {options[user]}")

if t1 == 0:
    print("It's a draw!")
elif t1 == 1:
    print("You won!")
else:
    print("You lost!")
