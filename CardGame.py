import random

suites =('heart' ,'diamond' ,'spade' ,'club')
ranks = ( 'two', 'three' ,'four' ,'five' ,'six' ,'seven' ,'eight', 'nine', 'ten', 'jack', 'queen', 'king' ,'ace')
values ={ 'two': 2, 'three':3 ,'four':4 ,'five': 5,'six':6 ,'seven':7 ,'eight':8, 'nine':9, 'ten':10, 'jack':10,'queen':10, 'king' :10,'ace':11 }
playing = True

class Card():
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
    def __str__(self):
         return self.rank + " of " + self.suite
       

class Deck:
    def __init__(self):
        self.deck=[]
        for suite in suites:
            for rank in ranks:
                self.deck.append(Card(suite, rank))
        

    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp +='\n' + card.__str__()
        return "The deck has " + deck_comp
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
       single_card = self.deck.pop()
       return single_card

# test_deck = Deck()
# print(test_deck)
# test_deck.shuffle()
# print(test_deck)

class Hand():
    def __init__(self):
        self.cards=[]
        self.value = 0
        self.aces=0

    def add_card(self, card):
        self.cards.append(card)
        self.value = values[card.rank] +self.value
        #track aces
        if card.rank =='ace':
            self.aces +=1

    def adjust_for_ace(self):
        #if total value >21 and I still have an ace then I use my ace as 1 instead of 11
        while self.value >21 and self.aces:
            self.value -=10
            self.aces -=1

test_deck = Deck()
test_deck.shuffle()

#Player

test_player = Hand()
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)
pulled_card2 = test_deck.deal()
test_player.add_card(pulled_card2)
print(test_player.value)
