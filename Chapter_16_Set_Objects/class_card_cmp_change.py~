# THIS CLASS CONSIDER THE ACE CARD OF ANY SUIT BIGGER THAN KING CARD OF ANY SUIT


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

    	if self.rank > other.rank: 						# THE BELOW CHUNK OF CODE ALLOW US COMPARE THE RANKS OF THE CARD CLASS
	    if other.rank==1:							# AND ALSO CONSIDER THE ACE'S CARDS GREATER THAN KING'S CARDS
		return -1
	    return 1	
    	if self.rank < other.rank: 				
	    if self.rank==1:
		return 1
	    return -1	
    # ranks are the same... it's a tie
     	return 0

