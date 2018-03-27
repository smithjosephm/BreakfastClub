from random import *


def calculateAmountWon(symbol, creditsplayed):
    if (symbol == "cherry"):
        return (creditsplayed * 5)
    if (symbol == "crown"):
        return (creditsplayed * 2.5)
    if (symbol == "bar"):
        return (creditsplayed * 1.5)


def play(money, creditsplayed):
    slot1 = choice(slotsPossible)
    slot2 = choice(slotsPossible)
    slot3 = choice(slotsPossible)
    slot4 = choice(slotsPossible)
    slot5 = choice(slotsPossible)
    slot6 = choice(slotsPossible)
    slot7 = choice(slotsPossible)
    slot8 = choice(slotsPossible)
    slot9 = choice(slotsPossible)
    lose = choice(Loser)
    winLineTop = False  # top horitontal
    winLineMiddle = False  # middle horizontal
    winLineBottom = False  # bottom horizontal
    winLine4DiagTop = False  # diagonal top to bottom
    winLine5DiagBot = False  # diagonal bottom to top
    winLineDiagBot = False #Diagonal win
    winLineDiagTop = False #Diagonal win
    winReel1 = False #Reel1 win
    winReel2 = False #Reel2 win
    winReel3 = False #Reel3 win
    winSymbol = ""
    winCount = 0
    winAmount = 0

    win = lose
    ##Top Lateral
    if (slot1 == slot2 == slot3):
        winLineTop = True
        winSymbol = slot1
        winAmount += calculateAmountWon(winSymbol, creditsplayed)
        winCount += 1

    ## diagonal top to bottom right
    if (slot1 == slot5 == slot9):
        winLineDiagTop = True
        winSymbol = slot1
        winAmount += calculateAmountWon(winSymbol, creditsplayed)
        winCount += 1
    ## Diagonal Bottom to top right
    if (slot7 == slot5 == slot3):
        winLineDiagBot = True
        winSymbol = slot7
        winAmount += calculateAmountWon(winSymbol, creditsplayed)
        winCount += 1
    ## Middle Lateral
    if (slot4 == slot5 == slot6):
        winLineMiddle = True
        winSymbol = slot4
        winAmount += calculateAmountWon(winSymbol, creditsplayed)
        winCount += 1
    ##Bottom Lateral
    if (slot7 == slot8 == slot9):
        winLineBottom = True
        winSymbol = slot7
        winAmount += calculateAmountWon(winSymbol, creditsplayed)
        winCount += 1
    ##Reel 1
    if (slot1 == slot4 == slot7):
        winReel1 = True
        winSymbol = slot1
        winAmount += calculateAmountWon(winSymbol, creditsplayed)
        winCount += 1
    ##Reel 2
    if (slot2 == slot5 == slot8):
        winReel2 = True
        winSymbol = slot2
        winAmount += calculateAmountWon(winSymbol, creditsplayed)
        winCount += 1
    ##Reel 3
    if (slot3 == slot6 == slot9):
        winReel3 = True
        winSymbol = slot2
        winAmount += calculateAmountWon(winSymbol, creditsplayed)
        winCount += 1
    # special case for all 3 lines winning
    if (winLineTop and winLineMiddle and winLineBottom):
        # add more winnings. we already counted these wins individually (5 wins), let's add another win for the bonus.
        winAmount += calculateAmountWon(winSymbol, creditsplayed)
        win = "\nYou win $%d. JACKPOT Bonus!" % (winAmount)
        currentmoney = winAmount +money
    if sum([winReel1,winReel2,winReel3,winLine4DiagTop,winLine5DiagBot,winLineBottom,winLineDiagBot,winLineDiagTop,winLineMiddle,winLineTop]) > 1:
        winAmount += calculateAmountWon(winSymbol, creditsplayed)
        win = "\nYou win $%d. MULTILINE Bonus!" % (winAmount)
        currentmoney = winAmount + money
    elif (winAmount > 0):
        win = "\nYou win $%d. !" % (winAmount)
        currentmoney = winAmount + money

    return slot1 + "|" + slot2 + "|" + slot3 + "\n" + slot4 + "|" + slot5 + "|" + slot6 + "\n" + slot7 + "|" + slot8 + "|" + slot9 + "\n" + win + "\n"
    return currentmoney

def gwaphics():
    slotsPossible = ["win", "cash", "money", "$$$$", "bar", "crown", "dollas"]
    slot1 = choice(slotsPossible)
    slot2 = choice(slotsPossible)
    slot3 = choice(slotsPossible)
    return slot1 + "|" + slot2 + "|" + slot3 + "\n" + slot1 + "|" + slot2 + "|" + slot3 + "\n" + slot1 + "|" + slot2 + "|" + slot3


print("Welcome to the Slot Machine!")
print (gwaphics())
money = int(input('How much cash do you want to put into the machine to play with?'))
creditsplayed = int(input('How much cash would you like to bet?'))
numberOfTimes = input('How many games would you like to play?')
slotsPossible = ["bar", "bar", "bar", "cherry", "crown", "crown"]
Loser = ["\nFEED ME MORE MONEY", "\nYa lose", "\nThanks dood", "\nHow's that retirement fund looking?"]
for i in range(int(numberOfTimes)):
    money = money - int(creditsplayed)
    print (play(money, creditsplayed))
    print ("You have "+str(money)+" left.\n")

