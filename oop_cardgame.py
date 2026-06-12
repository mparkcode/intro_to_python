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

    def deal(self):
        return self.cards.pop()

    # Magic __len__ method
    # If len is called on the Deck object anywhere, it will return the result of the __len__ method
    def __len__(self):
        return len(self.cards)

# Player Class
class Player:

    #constructor
    def __init__(self, name):
        self.name = name
        self.won_cards = []

    def collect(self, *cards):
        self.won_cards.extend(cards)

    def score(self):
        return len(self.won_cards)

class Game:

    #constructor
    def __init__(self):
        self.player1 = Player('Bill')
        self.player2 = Player('Bob')
        self.deck = Deck()

    def clear_screen(self):
        os.system('clear')

    def play_round(self):
        player1_card = self.deck.deal()
        player2_card = self.deck.deal()

        if player1_card.number > player2_card.number:
            print(f"{Fore.GREEN}{self.player1.name}'s card: {player1_card}")
            print(f"{Fore.RED}{self.player2.name}'s card: {player2_card}")

            print(f"{Fore.YELLOW}{self.player1.name} wins this hand!!")

            self.player1.collect(player1_card, player2_card)

        
        elif player1_card.number < player2_card.number:
            print(f"{Fore.RED}{self.player1.name}'s card: {player1_card}")
            print(f"{Fore.GREEN}{self.player2.name}'s card: {player2_card}")

            print(f"{Fore.YELLOW}{self.player2.name} wins this hand!!")

            self.player2.collect(player1_card, player2_card)


        else:
            print(f"{Fore.YELLOW}{self.player1.name}'s card: {player1_card}")
            print(f"{Fore.YELLOW}{self.player2.name}'s card: {player2_card}")

            print(f"{Fore.YELLOW}It's a DRAW!!")

            self.player1.collect(player1_card)
            self.player2.collect(player2_card)

    def display_results(self):
        p1_score = self.player1.score()
        p2_score = self.player2.score()

        if p1_score > p2_score:
            print(f"{Fore.YELLOW}{self.player1.name} wins the game with {p1_score} cards over {p2_score} cards!!")
        elif p1_score < p2_score:
            print(f"{Fore.YELLOW}{self.player2.name} wins the game with {p2_score} cards over {p1_score} cards!!")
        else:
            print(f"{Fore.YELLOW}It's a draw!!")

    def display_packs(self):
        self.clear_screen()
        print(f"{Fore.WHITE}{self.player1.name}'s cards:")
        for card in self.player1.won_cards:
            print(f"{Fore.MAGENTA}{card}")
        print(f"{Fore.WHITE}{self.player2.name}'s cards:")
        for card in self.player2.won_cards:
            print(f"{Fore.CYAN}{card}")
        


    def play(self):

        while len(self.deck) > 1:
            input(f"{Fore.WHITE}Press enter to deal cards.")

            self.clear_screen()
            self.play_round()

            print(f"{Fore.BLUE}Number of cards left {len(self.deck)}")

        self.display_results()

        show_packs = input(f"{Fore.WHITE}Would you like to see the players packs (y/n)?").upper()

        if show_packs == "Y":
            self.display_packs()

        print(f"{Fore.WHITE}Thanks for playing!!!")

new_game = Game()
new_game.play()