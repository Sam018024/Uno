##IMPORTS-------
import random
##--------------
##HARDCODEDLISTS
colours = ["Red", "Green", "Yellow", "Blue"]
colouredValues = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "+2"]
##--------------
##CLASSES-------
class Card(object):
    def __init__(self, colour, value):
        self.__colour = colour
        self.__value = value
        self.__filename = ""

    def __str__(self):
        string = str(self.__colour) + " " + str(self.__value)
        return string

    def setFilename(self):
        self.__filename = str(self.__colour) + "_" + str(self.__value) + ".png"

    def setColour(self, colour):
        self.__colour = colour

    def getValue(self):
        return self.__value

    def getColour(self):
        return self.__colour

    def getFilename(self):
        return self.__filename
##--------------
class Deck(object):
    def __init__(self):
        self.__cardList = []

    def createDeck(self):
        for i in range(0,len(colours)):
            card = Card(colours[i], "0")
            card.setFilename()
            self.__cardList.append(card)
        for h in range(0,2):
            for i in range(0,len(colouredValues)):
                for j in range(0,len(colours)):
                    card = Card(colours[j], colouredValues[i])
                    card.setFilename()
                    self.__cardList.append(card)
        for i in range(0,4):
            card = Card("Wild", "Wild")
            card.setFilename()
            self.__cardList.append(card)
            card = Card("Wild", "+4")
            card.setFilename()
            self.__cardList.append(card)
            

    def shuffleDeck(self):
        random.shuffle(self.__cardList)

    def getTopCard(self):
        if len(self.__cardList) > 0:
            return self.__cardList.pop(0)
        else:
            self.createDeck()
            self.shuffleDeck()
            return self.__cardList.pop(0)

    def getFirstNonWildCard(self):
        searching = True
        while searching == True:
            if len(self.__cardList) > 0:
                if self.__cardList[0].getColour() != "Wild":
                    searching = False
                    return self.__cardList.pop(0)
                else:
                    del self.__cardList[0]
            else:
                self.createDeck()
                self.shuffleDeck()
##--------------
class playerHand(object):
    def __init__(self, name):
        self.__playerName = str(name)
        self.__cardList = []

    def __str__(self):
        string = str(self.__playerName) + "'s hand"
        return string

    def getPlayerName(self):
        return self.__playerName

    def getCardList(self):
        return self.__cardList

    def drawStartingHand(self, deck):
        for i in range(0,7):
            self.__cardList.append(deck.getTopCard())

    def drawCard(self, deck):
        self.__cardList.append(deck.getTopCard())










        
