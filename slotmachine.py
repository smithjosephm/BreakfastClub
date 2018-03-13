from random import *

def play():
    slot1=choice(slotsPossible)
    slot2=choice(slotsPossible)
    slot3=choice(slotsPossible)
    lose = choice(Loser)
    win = lose
    if (slot1==slot2==slot3=="cherry"):
        win = "\nYou win $%d" % (creditsplayed * 10)
        if (creditsplayed * 10) == 20:
            win = "\nYou win $20. Aww $20? I wanted a peanut."
    if (slot1==slot2==slot3=="crown"):
        win = "\nYou win $%d" % (creditsplayed * 5)
        if (creditsplayed * 5) == 20:
            win = "\nYou win $20. Aww $20? I wanted a peanut."
    if (slot1==slot2==slot3=="bar"):
        win = "\nYou win $%d, not too bad." % (creditsplayed * 2)
        if (creditsplayed * 2) == 20:
            win = "\nYou win $20. Aww $20? I wanted a peanut."
    return slot1+":"+slot2+":"+slot3+" "+win

print("Welcome to the Slot Machine!")
creditsplayed = float(raw_input('How many credits would you like to bet?'))
numberOfTimes = input('How many games would you like to play?')
slotsPossible = ["bar","bar","bar","cherry","crown","crown"]
Loser = ["\nFEED ME MORE MONEY", "\nYa lose", "\nThanks dood", "\nHow's that retirement fund looking?"]

for i in range(int(numberOfTimes)):
    print(play())
