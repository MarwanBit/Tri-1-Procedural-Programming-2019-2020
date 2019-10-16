from card_class import Card 
from random import shuffle

class Shoe():
    def __init__(self, numDecks):
        self.cards = [Card(k%52) for k in range(numDecks*52)]
        shuffle(self.cards)
    def draw_a_card(self):
        return self.cards.pop()
    def deal(self,n):
        out = []
        for k in range(n):
            out.append(self.cards.pop())
        return out 
    def __getitem__(self,n):
        return self.cards[n]


if __name__ == "__main__":

    s = Shoe(1)
    hand = s.deal(5)
    for card in hand:
        print(card)

