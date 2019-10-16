class Card():
    def __init__(self, number):
        self.number = number 
    def rank(self):
        ranks = [
            "2","3","4","5","6","7",
            "8","9",'10',"J","Q","A"
            ]
        return ranks[self.number//4]
    def suit(self):
        suits = ["Clubs","Diamonds","Hearts","Spades"]
        return suits[self.number % 4]
    def __str__(self):
        return "Rank: {} of Suit: {}".format(self.rank(),self.suit())
    def __eq__(self,other):
        return self.number == other.number
    def __le__(self,other):
        '''Le redefines less than or equal to, evaluates self < other'''
        return self.number // 4  <= other.number // 4
    def __lt__(self,other):
        return self.number // 4 < other.number // 4
    def __ge__(self,other):
        return self.number // 4 >= other.number // 4 
    def __gt__(self,other):
        return self.number // 4 > other.number // 4
    def __repr__(self):
        '''Tells python how to rep this object in the interactive prompt'''
        return "'{} of {}'".format(self.rank(),self.suit())
    def __hash__(self):
        return self.number 
        

a = Card(28)
c = Card(29)
print(a <= c)
print(c <= a)
print(a,"\n",c)