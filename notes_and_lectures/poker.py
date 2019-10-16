from card_class import Card 
from decks_of_cards_shuffled_together import Shoe 
import itertools

def rank_concordence(hand):

    card_dictionary = {}

    for card in hand:
        if card.rank not in card_dictionary.keys():
            card_dictionary[card.rank] = 1 
        elif card in card_dictionary.keys():
            card_dictionary[card.rank] += 1  

    return card_dictionary
    

def num_different_ranks(hand):
    list_of_unique_ranks = set([i.rank() for i in hand])
    return len(list_of_unique_ranks)

def is_pair_only(hand):
    list_of_unique_ranks = [i.rank() for i in hand]
    list_of_unique_ranks = set(list_of_unique_ranks)
    return len(list_of_unique_ranks) == 4

def is_two_pairs_only(hand):
    if (len(list_of_unique_ranks) == 3):
        list_of_unique_ranks = set([i.rank() for i in hand])
        card_dictionary = rank_concordence(hand)
        if max(card_dictionary.values()) == 2:
            return True
    else:
        return False


def is_three_of_a_kind(hand):
    if (len(list_of_unique_ranks) == 3):
        list_of_unique_ranks = set([i.rank() for i in hand])
        card_dictionary = rank_concordence(hand)
        if max(card_dictionary.values()) == 3:
            return True
    else:
        return False


def is_full_house(hand):
    pass 

def is_four_of_a_kind(hand):
    pass 

def is_five_of_a_kind(hand):
    pass 

def is_flush(hand):
    pass

three = [Card(0),Card(1),Card(2),Card(28),Card(50)]
shoe = Shoe(1)
h = shoe.deal(5) 
print(is_pair_only(h))
