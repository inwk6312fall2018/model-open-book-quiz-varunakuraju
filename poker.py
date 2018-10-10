
import pyCardDeck
from pyCardDeck.cards import PokerCard


def deckcards():
        cards=[]
        deck_suit = ["Hearts","Spades","Clubs","Diamonds"]
        deck_value= {'1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten','J':'Jack','Q':'Queen','K':'King'}

        for item in deck_suit:
                for value,name in deck_value.items():
                        cards.append((item,name))
        print('Generated deck of cards for the table')

class PokerTable:

        def __init__(self, players):
                self.players = list(range(1,players))
                self.deck = pyCardDeck.Deck(cards=generate_initial_deck(),name='Poker Game',reshuffle=False)
                self.table_cards=[]
                self.hand = []
                print("This is a poker table with {} players".format(players))


        def texas_holdem(self):

                print("Starting a round of Texas Hold'em")
                self.deck.shuffle()
                self.draw_cards(2)

        def draw_cards(self, number):
                card = []
                for card in range(0, number):
                        for player in self.players:
                                card = self.deck.draw()
                                player.append(card)
                        print("Dealt {} to player {}".format(card, player))

                return cards

print(generate_initial_deck())
PT = PokerTable(5)
print(PT.draw_cards(5))
