"""
I am making a Blackjack game

We need to make cards and use random function and
assign a value to the cards and then compare it with 21.

I can use dictionary for assigning each card or use OOP to make cards then red or black,
then the four types of cards and then provide it with another list of objects of cards[such as ace,jack etc].
"""

import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank["rank"]
        self.value = rank["value"]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["spades", "diamonds", "clubs", "hearts"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                cards_dealt.append(self.cards.pop())
        return cards_dealt

class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards += card_list

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:

            self.value += card.value

            if card.rank == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10  # This is because the value of A varies regarding the value on hand between 1 and 11

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21

    def display(self, show_all_dealer_cards=False):
        print()

        print(f"""{"Dealer's " if self.dealer else "Your"} hand: """)

        for index, card in enumerate(self.cards):
            if (
                index == 0
                and self.dealer
                and not show_all_dealer_cards
                and not self.is_blackjack()
            ):
                print("HIDDEN")
            else:
                print(card)

        print()

        if not self.dealer:
            print("Value:", self.get_value())

        print()

class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play? "))
            except:
                print("You must input a positive integer.")

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""

            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:

                choice = str(input("Please choose 'Hit' or 'Stand': ")).lower()

                print()

                while choice not in ["s", "stand", "h", "hit"]:

                    choice = str(
                        input("Please enter 'Hit' or 'Stand' ( or H/S): ")
                    ).lower()

                    print()

                if choice in ["h", "hit"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()
                    print()

            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Your Hand:", player_hand_value)
            print("Dealer's Hand:", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, game_over=True)

        print("\n ❤️ !!!Thanks for playing!!! ❤️ \n")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You Busted!!! Dealer Wins!!! 😭")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer Busted!!! You Win!!! 🥳")
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("You both got 21!!! Draw!!! 😑 ")
                return True
            elif player_hand.is_blackjack():
                print("You have a blackjack!!! You Win!!! 🥳")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has a blackjack!!! You Lose!!! 😭")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You Win!!! 🥳")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("Draw!!! 😑")
            else:
                print("Dealer wins!!! 😭")
            return True
        return False

game = Game()
game.play()

print(help())