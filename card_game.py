import os
import random
from colorama import Fore

os.system('clear')

# Create our deck of cards
# shuffle it
# write logic to compare two card values
# winner will need to have both cards added to their decks

suits = ("Hearts", "Clubs", "Diamonds", "Spades")
numbers = range(2,15)

# required variables for the game
player1_card = None
player2_card = None

player1_pack = []
player2_pack = []

# Create our deck
def create_deck():
    deck = []
    for suit in suits:
        for number in numbers:
            card = (number, suit)
            deck.append(card)
    random.shuffle(deck)
    return deck

# function for processing face cards
def process_cards(card_number):
    face_cards = {
        "11": "Jack",
        "12": "Queen",
        "13": "King",
        "14": "Ace"
    }
    if str(card_number) in face_cards.keys():
        return face_cards[str(card_number)]
    else:
        return str(card_number)

my_deck = create_deck()

# main game loop
while len(my_deck) > 1:

    input(f"{Fore.WHITE}Press enter to deal cards")
    
    
    player1_card = my_deck.pop()
    player2_card = my_deck.pop()

    p1_card_name = process_cards(player1_card[0])
    p2_card_name = process_cards(player2_card[0])
    
    if player1_card[0] > player2_card[0]:
        #display cards
        print(f"{Fore.GREEN}Player 1 card: {p1_card_name} of {player1_card[1]}")
        print(f"{Fore.RED}Player 2 card: {p2_card_name} of {player2_card[1]}")

        print(f"{Fore.YELLOW}Player 1 wins this hand!!")

        player1_pack.append(player1_card)
        player1_pack.append(player2_card)


    elif player1_card[0] < player2_card[0]:
        #display cards
        print(f"{Fore.RED}Player 1 card: {p1_card_name} of {player1_card[1]}")
        print(f"{Fore.GREEN}Player 2 card: {p2_card_name} of {player2_card[1]}")

        print(f"{Fore.YELLOW}Player 2 wins this hand!!")

        player2_pack.append(player1_card)
        player2_pack.append(player2_card)

    else:
        #display cards
        print(f"{Fore.YELLOW}Player 1 card: {p1_card_name} of {player1_card[1]}")
        print(f"{Fore.YELLOW}Player 2 card: {p2_card_name} of {player2_card[1]}")

        print(f"{Fore.YELLOW}It's a draw!!")

        player1_pack.append(player1_card)
        player2_pack.append(player2_card)

    print(f"{Fore.BLUE}Number of cards left: {len(my_deck)}")

# determine a winner
if len(player1_pack) > len(player2_pack):
    print(f"Player 1 wins the game with {len(player1_pack)} cards over {len(player2_pack)} cards!")
elif len(player1_pack) < len(player2_pack):
    print(f"Player 2 wins the game with {len(player2_pack)} cards over {len(player1_pack)} cards!")
else:
    print("It's a Draw!")

if input(f"{Fore.WHITE}Would you like to see the players' packs (y/n)?").upper() == 'Y':
    print(f'{Fore.WHITE}Player 1 pack: ')
    for card in player1_pack:
        print(f"{Fore.MAGENTA} {process_cards(card[0])} of {card[1]}")
    print(f'{Fore.WHITE}Player 2 pack: ')
    for card in player2_pack:
        print(f"{Fore.CYAN} {process_cards(card[0])} of {card[1]}")
    
print(f"{Fore.WHITE}Thanks for playing!!")