import random
import sys


def getCardValue():
    # returns a number with a specific range from 2 to 14.
    return random.randint(2, 14)


def getCardStr(cardValue):
    ten = "T"
    jack = "J"
    queen = "Q"
    king = "K"
    ace = "A"
    if 2 <= cardValue <= 9:
        return str(cardValue)
    elif cardValue == 10:
        return ten
    elif cardValue == 11:
        return jack
    elif cardValue == 12:
        return queen
    elif cardValue == 13:
        return king
    else:
        return ace


def getHLGuess():
    twoChoices = ("HIGHER", "LOWER")
    # a tuple of two strings
    otherInput = random.choice(twoChoices)
    # randomly picks one of the 2 strings from the tuple.

    playerGuess = input('Higher or Lower (H/L)? Any other input will be randomly picked.')
    if playerGuess == 'h' or playerGuess == 'H':
        return "HIGHER"
    elif playerGuess == 'l' or playerGuess == 'L':
        return "LOWER"
    else:
        # if the input is not "h" or "l" (lowercase or uppercase), it randomly picks a string from the tuple.
        return otherInput


def getBetAmount(maximum):
    playerBet = 1

    while playerBet > 0 or playerBet < maximum:
        try:
            playerBet = int(input("Please put in your bet amount: "))
            if playerBet > maximum:
                print("You cannot bet anything higher than your current points.")
            elif playerBet <= 0:
                print("Anything zero or less is an invalid bet.")
            else:
                return playerBet
        except ValueError:
            print("Invalid bet. Must be a number. (From 1 to your current points)")


def playerGuessCorrect(card1, card2, betType):
    if betType == "HIGHER" and card2 > card1:
        # if the bet type is selected "higher" and the second card is higher than the first card, return true.
        return True
    elif betType == "LOWER" and card2 < card1:
        # if the bet type is selected "lower" and the second card is lower than the first card, return true.
        return True
    else:
        # if any of the two statements are not true, return false.
        return False


# main driver for the program.
def main():
    welcomeText = """
-- Welcome to Higher or Lower! --
You start off with 100 points. Each round a card will be drawn and shown.
Select whether you think the 2nd card will be Higher or Lower than the 1st card. 
Then enter the amount you want to bet.
If you are right, you win the amount you bet, otherwise you lose.
Try to make it to 500 points within 10 rounds.
"""
    print(welcomeText)

    roundCounter = 1
    # the starting number of rounds, up to 10 rounds.
    pointsCounter = 100
    # the starting number of points the player starts with.

    while roundCounter < 11 and 500 > pointsCounter > 0:
        # a loop when the round is still less than 11 (up to Round 10), while the number of points is less than 500,
        # and greater than 0.
        print("---------------------------------------")
        print("Your current points: " + str(pointsCounter) + " (ROUND " + str(roundCounter) + "/10)")
        # gets the first card, then asks the player for a guess and a bet for the second card.
        card1 = getCardValue()
        firstCard = getCardStr(card1)
        print("The first card is: " + firstCard)
        betType = getHLGuess()
        playerBet = getBetAmount(pointsCounter)

        # gets the second card.
        card2 = getCardValue()
        secondCard = getCardStr(card2)
        print("The second card is: " + secondCard)

        if playerGuessCorrect(card1, card2, betType):
            # if the player guesses correctly, it displays a message and add points how much the player had bet on.
            print("---------------------------------------")
            print("First card: " + firstCard + " Second Card: " + secondCard)
            print("You bet " + betType + " for: " + str(playerBet))
            print("You have won this round!")
            print("---------------------------------------")
            pointsCounter += playerBet
            roundCounter += 1
        else:
            # if the player guesses incorrectly, it displays a message and lose points how much the player had bet on.
            print("---------------------------------------")
            print("First card: " + firstCard + ", and Second Card: " + secondCard)
            print("You bet " + betType + " for: " + str(playerBet))
            print("You have lost this round.")
            print("---------------------------------------")
            pointsCounter -= playerBet
            roundCounter += 1

    if pointsCounter >= 500:
        # if the player gets to 500 points or more on any round up to Round 10, they win.
        print("---------------------------------------")
        print(
            "You have made it to 500 points (or greater) in", roundCounter - 1,
            "rounds! \nYou won the game! Congratulations!")
        print("---------------------------------------")
    elif pointsCounter <= 0:
        # if the player has 0 points or fewer on any round up to Round 10, they lose.
        print("---------------------------------------")
        print("You have zero points after", roundCounter - 1, "rounds! \nYou lose!")
        print("---------------------------------------")
    else:
        # if the player reaches to Round 10 without achieving the winning score, they also lose.
        print("---------------------------------------")
        print("You only have " + str(pointsCounter) + " points in 10 rounds! \nYou lose!")
        print("---------------------------------------")


# restart function
restart = ""

if __name__ == "__main__":
    while True:
        main()
        restart = input("Do you want to restart? [Y/N]")
        if restart == "y" or restart == "Y":
            continue
        else:
            print("Now closing the game...")
            sys.exit(0)
