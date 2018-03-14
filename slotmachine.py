from random import *

def play():
    slot1= choice(slotsPossible)
    slot2= choice(slotsPossible)
    slot3= choice(slotsPossible)
    slot4 = choice(slotsPossible)
    slot5 = choice(slotsPossible)
    slot6 = choice(slotsPossible)
    slot7 = choice(slotsPossible)
    slot8 = choice(slotsPossible)
    slot9 = choice(slotsPossible)
    lose = choice(Loser)
    win = lose
    if (slot1==slot2==slot3=="cherry"):
        win = "\nYou win $%d" % (creditsplayed * 10)
    ##Top Lateral
    if (slot1 == slot5 == slot9 == "cherry"):
        win = "\nYou win $%d" % (creditsplayed * 10)
    ## diagonal top to bottom right
    if (slot7 == slot5 == slot3 == "cherry"):
        win = "\nYou win $%d" % (creditsplayed * 10)
    ## Diagonal Bottom to top right
    if (slot4==slot5==slot6=="cherry"):
        win = "\nYou win $%d" % (creditsplayed * 10)
    ## Middle Lateral
    if (slot7 == slot8 == slot9 == "cherry"):
        win = "\nYou win $%d" % (creditsplayed * 10)
    ##Bottom Lateral
    if (slot1 == slot2 == slot3 == "cherry") and (slot4 == slot5 == slot6 == "cherry") and (slot7 == slot8 == slot9 == "cherry"):
        win = "\nYou win $%d. JACKPOT Bonus!" % (6 * (creditsplayed * 10))
    ## All Lateral
    if (slot1==slot2==slot3=="cherry") and (slot1 == slot5 == slot9 == "cherry"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 10))
    ##Top Lateral, Diagonal Top to bottom right
    if (slot1 == slot2 == slot3 == "cherry") and (slot4 == slot5 == slot6 == "cherry"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 10))
    ##Top Lateral, Middle Lateral.
    if (slot1 == slot2 == slot3 == "cherry") and (slot7 == slot8 == slot9 == "cherry"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 10))
    ## Top Lateral, Middle Lateral
    if (slot1 == slot2 == slot3 == "cherry") and (slot1 == slot5 == slot9 == "cherry"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 10))
    ##Top Lateral, Diagonal top to bottom
    if (slot1 == slot2 == slot3 == "cherry") and (slot7 == slot5 == slot3 == "cherry"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 10))
    ##Top Lateral Diagonal Bottom to top
    if (slot4==slot5==slot6=="cherry") and (slot1 == slot2 == slot3 == "cherry"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 10))
    ##Middle Lateral, top lateral
    if (slot4==slot5==slot6=="cherry") and (slot7 == slot8 == slot9 == "cherry"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 10))
    ##Middle Lateral, bottom lateral
    if (slot4==slot5==slot6=="cherry") and (slot1 == slot5 == slot9 == "cherry"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 10))
    ##Middle Lateral, Diagonal
    if (slot4==slot5==slot6=="cherry") and (slot1 == slot5 == slot9 == "cherry"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 10))
    #Middle Lateral, Diagonal top to bottom
    if (slot4==slot5==slot6=="cherry") and (slot7 == slot5 == slot3 == "cherry"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 10))
    ##Middle Lateral, bottom to top
    if (slot7==slot8==slot9=="cherry") and (slot1 == slot2 == slot3 == "cherry"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 10))
    ##Bottom Lateral, Top Lateral
    if (slot7==slot8==slot9=="cherry") and (slot4 == slot5 == slot6 == "cherry"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 10))
    ##Bottom Lateral, Middle Lateral
    if (slot7==slot8==slot9=="cherry") and (slot7 == slot5 == slot3 == "cherry"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 10))
    ##Bottom lateral, diagonal to top
    if (slot7==slot8==slot9=="cherry") and (slot1 == slot5 == slot9 == "cherry"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 10))
    ## Bottom Lateral, diagonal from top
    ##Bottom Lateral
    if (slot1 == slot2 == slot3 == "crown") and (slot4 == slot5 == slot6 == "crown") and (slot7 == slot8 == slot9 == "crown"):
        win = "\nYou win $%d. JACKPOT Bonus!" % (6 * (creditsplayed * 5))
    ## All Lateral
    if (slot1==slot2==slot3=="crown") and (slot1 == slot5 == slot9 == "crown"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 5))
    ##Top Lateral, Diagonal Top to bottom right
    if (slot1 == slot2 == slot3 == "crown") and (slot4 == slot5 == slot6 == "crown"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 5))
    ##Top Lateral, Middle Lateral.
    if (slot1 == slot2 == slot3 == "crown") and (slot7 == slot8 == slot9 == "crown"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 5))
    ## Top Lateral, bottom Lateral
    if (slot1 == slot2 == slot3 == "crown") and (slot1 == slot5 == slot9 == "crown"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 5))
    ##Top Lateral, Diagonal top to bottom
    if (slot1 == slot2 == slot3 == "crown") and (slot7 == slot5 == slot3 == "crown"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 5))
    ##Top Lateral Diagonal Bottom to top
    if (slot4==slot5==slot6=="crown") and (slot1 == slot2 == slot3 == "crown"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 5))
    ##Middle Lateral, top lateral
    if (slot4==slot5==slot6=="crown") and (slot7 == slot8 == slot9 == "crown"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 5))
    ##Middle Lateral, bottom lateral
    if (slot4==slot5==slot6=="crown") and (slot1 == slot5 == slot9 == "crown"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 5))
    ##Middle Lateral, Diagonal
    if (slot4==slot5==slot6=="crown") and (slot1 == slot5 == slot9 == "crown"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 5))
    #Middle Lateral, Diagonal top to bottom
    if (slot4==slot5==slot6=="crown") and (slot7 == slot5 == slot3 == "crown"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 5))
    ##Middle Lateral, bottom to top
    if (slot7==slot8==slot9=="crown") and (slot1 == slot2 == slot3 == "crown"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 5))
    ##Bottom Lateral, Top Lateral
    if (slot7==slot8==slot9=="crown") and (slot4 == slot5 == slot6 == "crown"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 5))
    ##Bottom Lateral, Middle Lateral
    if (slot7==slot8==slot9=="crown") and (slot7 == slot5 == slot3 == "crown"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 5))
    ##Bottom lateral, diagonal to top
    if (slot7==slot8==slot9=="crown") and (slot1 == slot5 == slot9 == "crown"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 5))
    ## Bottom Lateral, diagonal from top
    ##Bottom Lateral
    if (slot1 == slot2 == slot3 == "bar") and (slot4 == slot2 == slot6 == "bar") and (slot7 == slot8 == slot9 == "bar"):
        win = "\nYou win $%d. JACKPOT Bonus!" % (6 * (creditsplayed * 2))
    ## All Lateral
    if (slot1==slot2==slot3=="bar") and (slot1 == slot5 == slot9 == "bar"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 2))
    ##Top Lateral, Diagonal Top to bottom right
    if (slot1 == slot2 == slot3 == "bar") and (slot4 == slot5 == slot6 == "bar"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 2))
    ##Top Lateral, Middle Lateral.
    if (slot1 == slot2 == slot3 == "bar") and (slot7 == slot8 == slot9 == "bar"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 2))
    ## Top Lateral, Middle Lateral
    if (slot1 == slot2 == slot3 == "bar") and (slot1 == slot2 == slot9 == "bar"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 2))
    ##Top Lateral, Diagonal top to bottom
    if (slot1 == slot2 == slot3 == "bar") and (slot7 == slot2 == slot3 == "bar"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 2))
    ##Top Lateral Diagonal Bottom to top
    if (slot4==slot2==slot6=="bar") and (slot1 == slot2 == slot3 == "bar"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 2))
    ##Middle Lateral, top lateral
    if (slot4==slot2==slot6=="bar") and (slot7 == slot8 == slot9 == "bar"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 2))
    ##Middle Lateral, bottom lateral
    if (slot4==slot2==slot6=="bar") and (slot1 == slot2 == slot9 == "bar"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 2))
    ##Middle Lateral, Diagonal
    if (slot4==slot2==slot6=="bar") and (slot1 == slot2 == slot9 == "bar"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 2))
    #Middle Lateral, Diagonal top to bottom
    if (slot4==slot2==slot6=="bar") and (slot7 == slot2 == slot3 == "bar"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 2))
    ##Middle Lateral, bottom to top
    if (slot7==slot8==slot9=="bar") and (slot1 == slot2 == slot3 == "bar"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 2))
    ##Bottom Lateral, Top Lateral
    if (slot7==slot8==slot9=="bar") and (slot4 == slot2 == slot6 == "bar"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 2))
    ##Bottom Lateral, Middle Lateral
    if (slot7==slot8==slot9=="bar") and (slot7 == slot2 == slot3 == "bar"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 2))
    ##Bottom lateral, diagonal to top
    if (slot7==slot8==slot9=="bar") and (slot1 == slot2 == slot9 == "bar"):
        win = "\nYou win $%d. Multiline Bonus!" % (2 * (creditsplayed * 2))
    ## Bottom Lateral, diagonal from top
    if (slot1==slot2==slot3=="crown") or (slot1 == slot5 == slot9 == "crown") or (slot7 == slot5 == slot3 == "crown") or (slot4==slot5==slot6=="crown") or (slot7==slot8==slot9=="crown"):
        win = "\nYou win $%d" % (creditsplayed * 5)
        if (creditsplayed * 5) == 20:
            win = "\nYou win $20. Aww $20? I wanted a peanut."
    if (slot1==slot2==slot3=="bar") or (slot1 == slot5 == slot9 == "bar") or (slot7 == slot5 == slot3 == "bar") or (slot4==slot5==slot6=="bar") or (slot7==slot8==slot9=="bar"):
        win = "\nYou win $%d, not too bad." % (creditsplayed * 2)
        if (creditsplayed * 2) == 20:
            win = "\nYou win $20. Aww $20? I wanted a peanut."
    return slot1+"|"+slot2+"|"+slot3+"\n"+slot4+"|"+slot5+"|"+slot6+"\n"+slot7+"|"+slot8+"|"+slot9+"\n"+ win + "\n"

def gwaphics():
    slotsPossible = ["win", "cash", "money", "$$$$", "bar", "crown","dollas"]
    slot1 = choice(slotsPossible)
    slot2 = choice(slotsPossible)
    slot3 = choice(slotsPossible)
    return slot1+"|"+slot2+"|"+slot3+"\n"+slot1+"|"+slot2+"|"+slot3+"\n"+slot1+"|"+slot2+"|"+slot3


print("Welcome to the Slot Machine!")
print gwaphics()
creditsplayed = float(raw_input('How many credits would you like to bet?'))
numberOfTimes = input('How many games would you like to play?')
slotsPossible = ["bar","bar","bar","cherry","crown","crown"]
Loser = ["\nFEED ME MORE MONEY", "\nYa lose", "\nThanks dood", "\nHow's that retirement fund looking?"]

for i in range(int(numberOfTimes)):
    print(play())

