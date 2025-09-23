##IMPORTS-------
import initialisation
import random
##--------------
##INITIALVALUES-
Choice = "-1"
##--------------
##MAINPROGRAM---
while Choice != "0":
    print("""----UNO----
1 - Play!
0 - Exit...
-----------""")
    Choice = str(input())
    
    if Choice == "0":
        Choice = "0"
        
    elif Choice == "1":
        Deck = initialisation.Deck()
        Deck.createDeck()
        Deck.shuffleDeck()
        playerList = []
        
        question = True
        while question == True:
            try:
                playerCount = int(input("How many players? (2-7): "))
                if playerCount > 7 or playerCount < 2:
                    print(playerCount, "is an invalid amount of players")
                else:
                    question = False
            except:
                print("That is an invalid option")
                
        num = 0
        for i in range(0,playerCount):
            num = i + 1
            username = input("What is player " + str(num) + "'s name: ")
            playerHand = initialisation.playerHand(username)
            playerHand.drawStartingHand(Deck)
            playerList.append(playerHand)

        discardPile = [Deck.getFirstNonWildCard()]
        print(discardPile[0])
        
        gamePlaying = True
        playerNum = -1
        orderOfPlay = 1
        while gamePlaying == True:
            going = None
            numberOfPlayers = len(playerList) - 1
            playerNum += orderOfPlay
            if playerNum > numberOfPlayers:
                playerNum -= (numberOfPlayers + 1)
            elif playerNum < 0:
                playerNum += (numberOfPlayers + 1)
            print("It's " + str(playerList[playerNum].getPlayerName()) + "'s go!")
            playerName = str(playerList[playerNum].getPlayerName()).upper()
            print(playerName + "'S HAND:")
            for j in range(0,len(playerList[playerNum].getCardList())):
                num = j + 1
                print(num, playerList[playerNum].getCardList()[j])
                if playerList[playerNum].getCardList()[j].getColour() == discardPile[0].getColour() or playerList[playerNum].getCardList()[j].getValue() == discardPile[0].getValue() or playerList[playerNum].getCardList()[j].getColour() == "Wild":
                    going = True
            if going != True:
                print(playerName, "could not go, they drew a card")
                playerList[playerNum].drawCard(Deck)
            print("The card on top of the discard pile is", discardPile[0])
            while going == True:
                action = input("Give the number of the card you would like to play: ")
                try:
                    action = int(action)
                    print("conversion")
                    action2 = action
                    print("action2 = action")
                    action -= 1
                    print("action -= 1")
                    if playerList[playerNum].getCardList()[action].getColour() == discardPile[0].getColour() or playerList[playerNum].getCardList()[action].getValue() == discardPile[0].getValue() or playerList[playerNum].getCardList()[action].getColour() == "Wild":
                        del discardPile[0]
                        playedCard = playerList[playerNum].getCardList()[action]
                        del playerList[playerNum].getCardList()[action]
                        discardPile.append(playedCard)
                        if discardPile[0].getValue() == "Skip":
                            tempplayerNum = playerNum + orderOfPlay
                        elif discardPile[0].getValue() == "Reverse":
                            orderOfPlay *= -1
                        elif discardPile[0].getValue() == "+2":
                            playerTarget = playerNum + orderOfPlay
                            if playerTarget > numberOfPlayers:
                                playerTarget -= (numberOfPlayers + 1)
                            elif playerTarget < 0:
                                playerTarget += (numberOfPlayers + 1)
                            for i in range(0,2):
                                playerList[playerTarget].drawCard(Deck)
                        elif discardPile[0].getValue() == "+4":
                            playerTarget = playerNum + orderOfPlay
                            if playerTarget > numberOfPlayers:
                                playerTarget -= (numberOfPlayers + 1)
                            elif playerTarget < 0:
                                playerTarget += (numberOfPlayers + 1)
                            for i in range(0,4):
                                playerList[playerTarget].drawCard(Deck)
                        else:
                            print("If you see this something has gone wrong with the value check or it is a number")
                        if discardPile[0].getColour() == "Wild":
                            choosingColour = True
                            print("""PICK A COLOUR
1 - Red
2 - Green
3 - Yellow
4 - Blue""")
                            while choosingColour == True:
                                colourChoice = str(input("Colour: "))
                                if colourChoice == "1":
                                    discardPile[0].setColour("Red")
                                    choosingColour = False
                                elif colourChoice == "2":
                                    discardPile[0].setColour("Green")
                                    choosingColour = False
                                elif colourChoice == "3":
                                    discardPile[0].setColour("Yellow")
                                    choosingColour = False
                                elif colourChoice == "4":
                                    discardPile[0].setColour("Blue")
                                    choosingColour = False
                                else:
                                    print(colourChoice, "is not a valid answer")
                        else:
                            print("Wild Check")
                        
                        if len(playerList[playerNum].getCardList()) == 0:
                            gamePlaying = False
                            print(playerList[playerNum].getPlayerName(), "has won")
                        try:
                            playerNum = tempplayerNum
                            tempplayerNum = None
                        except:
                            temp = 0
                            print(temp)
                        going = False                   
                        
                    else:
                        print(playerList[playerNum].getCardList()[action], "is not a legal move")
                except:
                    print(action2, "is not a valid go.")
                
                
                
    else:
        print(Choice, "isn't an option")


