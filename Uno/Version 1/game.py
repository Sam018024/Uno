import random
import time
import initialisation

def nextPlayer(playerNum, numOfPlayers, order):
    playerNum += order
    if playerNum > (numOfPlayers - 1):
        playerNum -= numOfPlayers
    elif playerNum < 0:
        playerNum += numOfPlayers
    return playerNum
       

def Game():
    Deck = initialisation.Deck()
    Deck.createDeck()
    Deck.shuffleDeck()
    playerList = []
    colourList = ["Red", "Green", "Yellow", "Blue"]

    playerQuestion = True
    while playerQuestion == True:
        try:
            playerCount = int(input("How many players? (2-7): "))
            if playerCount > 7 or playerCount < 2:
                print(playerCount, "is and invalid amount of players")
            else:
                playerQuestion = False
        except:
            print("That is an invalid option")

    for i in range(0, playerCount):
        username = input("What is player " + str(i+1) + "'s name: ")
        playerHand = initialisation.playerHand(username)
        playerHand.drawStartingHand(Deck)
        playerList.append(playerHand)

    discardPile = [Deck.getFirstNonWildCard()]
    print("--------------------------")

    gamePlaying = True
    playerNum = -1
    orderOfPlay = 1
    tempPlayerNum = None
    
    while gamePlaying == True:
        time.sleep(1)
        ableToGo = None
        playerNum = nextPlayer(playerNum, len(playerList), orderOfPlay)
        
        print("It's " + str(playerList[playerNum].getPlayerName()) + "'s go!")

        print(str(playerList[playerNum].getPlayerName()).upper() + "'S HAND:")
        for i in range(0, len(playerList[playerNum].getCardList())):
            currentCard = playerList[playerNum].getCardList()[i]
            print((i + 1), "-", currentCard)
            if currentCard.getColour() == discardPile[0].getColour() or currentCard.getValue() == discardPile[0].getValue() or currentCard.getColour() == "Wild":
                ableToGo = True
                
        if ableToGo != True:
            print(playerList[playerNum].getPlayerName(), "could not go, they drew a card")
            playerList[playerNum].drawCard(Deck)
            print("--------------------------")

        while ableToGo == True:
            print("The card on top of the discard pile is", discardPile[0])
            try:
                cardChoice = int(input("Give the number of the card you would like to play: "))
                cardChoice -= 1
                currentPlayer = playerNum

                playedCard = playerList[playerNum].getCardList()[cardChoice]
                if playedCard.getColour() == discardPile[0].getColour() or playedCard.getValue() == discardPile[0].getValue() or playedCard.getColour() == "Wild":
                    del discardPile[0]
                    del playerList[playerNum].getCardList()[cardChoice]
                    discardPile.append(playedCard)
                    
                    if discardPile[0].getValue() == "Skip":
                        playerNum = nextPlayer(playerNum, len(playerList), orderOfPlay)

                    elif discardPile[0].getValue() == "Reverse":
                        if playerCount == 2:
                            playerNum = nextPlayer(playerNum, len(playerList), orderOfPlay)
                        orderOfPlay *= -1

                    elif discardPile[0].getValue()[0] == "+":
                        playerNum = nextPlayer(playerNum, len(playerList), orderOfPlay)
                        for i in range(0, int(discardPile[0].getValue()[1])):
                            playerList[playerNum].drawCard(Deck)

                    if discardPile[0].getColour() == "Wild":
                        choosingColour = True
                        print("""PICK A COLOUR
1 - Red
2 - Green
3 - Yellow
4 - Blue""")
                        while choosingColour == True:
                            try:
                                colourChoice = int(input("Colour: "))
                                if colourChoice < 1 or colourChoice > 4:
                                    print("Please choose the number next to your desired colour")
                                else:
                                    discardPile[0].setColour(colourList[colourChoice-1])
                                    choosingColour = False
                            except:
                                print("Please enter a number")

                    if len(playerList[currentPlayer].getCardList()) == 0:
                        gamePlaying = False
                        print(playerList[currentPlayer].getPlayerName(), "has won!")
                        for i in range(0,100):
                            print()
                    ableToGo = False
                    print("--------------------------")
                else:
                    print(playedCard, "is not a legal play")
                
                
            except:
                print("That is not a valid option")

        
                    


















            
            
