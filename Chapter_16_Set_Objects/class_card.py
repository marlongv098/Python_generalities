# WE CAN ALSO DEFINED THE SUITS AND RANKS LIKE LINKED LIST. i.e. USING LEVELS FOR THE SUITS 

# Spades   -->  3
# Hearts   -->  2
# Diamonds -->  1
# Clubs    -->  0

# AND LEVELS FOR RANKS

# Jack   -->  11
# Queen  -->  12
# King   -->  13 
# 
# ETC...
# IN THIS CLASS THE SUITS AND RANKS WERE DEFINED USING LIST. THE PARTICULARITY IS THAT THE LIST HAVE INDEXES AND WE WORKS WHIT THEM


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

    def __cmp__(self, other):							# THIS FUNCTION COMPARE TWO CARDS BASED ON THE LEVEL LIST
    # check the suits
    	if self.suit > other.suit: return 1					# EACH LINE RETURN 1 OR -1 DEPEND ON THE CASE 
    	if self.suit < other.suit: return -1					
    # suits are the same... check ranks						# WHEN THAY ARE THE SAME LEVEL SUIT IT WILL BE CONSIDERED THE RANK
    	if self.rank > other.rank: return 1
    	if self.rank < other.rank: return -1
    # ranks are the same... it's a tie
     	return 0

  

card1 = Card(0,1)
card2 = Card(1,2)
card3 = Card(3,11)
card4 = Card(3,10)
card5 = Card(3,10)
print card1
print card2
print card3
print cmp(card1,card2)
print cmp(card1,card3)
print cmp(card2,card3)
print cmp(card3,card2)
print cmp(card3,card4)
print cmp(card4,card5)
