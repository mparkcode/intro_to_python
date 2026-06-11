import os
import random
from colorama import Fore

os.system("clear")

# Classes! Card Deck Player Game

# Card Class
class Card:

    #constructor
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    @property
    def name(self):
        
        face_cards = {
            "11": "Jack",
            "12": "Queen",
            "13": "King",
            "14": "Ace"
        }

        return face_cards.get(str(self.number), str(self.number))


    # Magic string method
    def __str__(self):
        return f"{self.name} of {self.suit}"

# Deck Class
class Deck:
    #class attributes
    SUITS = ("Hearts", "Clubs", "Diamonds", "Spades")

    #constructor
    def __init__(self):
        self.cards = []

        for suit in self.SUITS:
            for number in range(2,15):
                card = Card(number, suit)
                self.cards.append(card)

        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)

# Player Class
class Player:

    #constructor
    def __init__(self, name):
        self.name = name
        self.won_cards = []