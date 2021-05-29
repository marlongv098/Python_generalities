

class Card():
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]				# LEVEL LISTS
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"] 	# THE narf ELEMENT IS WAS DEFINED BY CONVIENCE

    def __init__(self, suit=0, rank=0):						# INITIALIZATION METHOD TO THE CLASS AS USUAL
        self.suit = suit							# HERE IT TAKES INDEXES OF THE LISTS
        self.rank = rank							

    def __str__(self):								# str METHOD
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])		# HERE IT WAS USED THE init FUNCTION AND THE INDEXES LIST
										# THE self.ranks PRINT THE NAME INSIDE THE RANKS LIST.
    									 	# self.rank IS THE NUMBER GIVEN TO THE init FUNCTION. . 
										# THE SAME FOR self.suits 

# FUNCTION WHICH CREATES THE THE DECK. (MEANING OF DECK = BARAJA)


class Deck:
    def __init__(self):
        self.cards = []						# HERE IT WILL BE STORE THE DECK ELEMENTS
        for suit in range(4):					# THE DECK HAS 4 SUITS
            for rank in range(1, 14):				# AND THIRTEEN RANKS FROM 1 TO 13.
                self.cards.append(Card(suit, rank))		# THE DECK IT WAS STORE IN A LIST OF FOUR LIST EACH ONE OF THEM HAVE THRITEEN ELEMENTS

    def print_deck(self):					# THIS FUNCTION PRINT THE STORE DECK 
        for card in self.cards:					# THIS FUNCTION IS LESS FLEXIBLE THAN THE BELOW
            print card

    def __str__(self):						# THIS FUNCTION IS AN ALTERNATIVE TO THE ABOVE FUNCTION print_deck 
        s = ""							# ONE OF THE ADVANTAGES OF THIS KIND OF FUNCTION IT IS MORE FLEXIBLE..
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"		# THIS LINE PRINT THE STRING BUT ALSO IN EACH LINE PRINT ' ' * i SPACES
        return s						# 


    def shuffle(self):
        import random
        num_cards = len(self.cards)				# LEN OF THE SHUFFLE DECK
	s = ""							# EMPTY STRING
        for i in range(num_cards):				# 
            j = random.randrange(i, num_cards)			# 
	    self.cards[i], self.cards[j] = self.cards[j], self.cards[i]	# THIS LINE SWAP THE CURRENT CARD i-TH WITH THE SELECTED CARD j-TH.TO AVOID PRINT A SAME CARD IN THE SHUFFLE DECK. i.e. WE TAKE THE i-TH POSITION AND PUT THERE THE j-TH CARD AND IN THE j-TH PLACE WE PUT THE i-TH CARD.
	    
	    #s = s + str(self.cards[i]) + "\n"			# SAME LINE OF THE FUNCTION ABOVE.
	#return s						# TO WORK WITH THE REMOVE FUNCTION INSIDE THE CLASS WE CAN NOT USE THE THESE LINES. 

    def remove(self, card):					# THIS FUNCTION TAKES THE DECK AND REMOVES A CARD FROM IT.
        if card in self.cards:	
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()					# THIS LINE PRINTS THE HIGHEST DECK ELEMENT

    def is_empty(self):	
        return (len(self.cards) == 0)				# THIS IS USED WHEN THE LEN'S DECK ==0, i.e. AFTER REMOVE EACH ELEMENT OF THE DECK.


deck = Deck()
#print deck.print_deck()					# USE print_deck FUNCTION
#print deck							# USE str FUNCTION
card=Card(1,1)
card1=Card(2,1)
#print deck.shuffle()						# TO USE THIS ONE WE HAVE TO DEFINE RETURN OF SHUFFLE FUNCTION INSIDE THE DECK CLASS. 
#dec=deck.shuffle()
#print deck.remove(card1)
#print deck.remove(card)

print deck.pop()
