# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []
        pass	# create Hand object

    def __str__(self):
        ans = ""
        for i in range(len(self.hand)):
            ans += str(self.hand[i]) + " "
        return "Hand contains " + ans
        
        pass	# return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)
        pass	# add a card object to a hand

    def get_value(self):
        value = 0
        for n in self.hand:
            value += VALUES[n.get_rank()]
        if value + 10 <= 21:
            return value + 10
      
        else:
            return value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        pass	# compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for c in range(len(self.hand)):
            self.hand[c].draw(canvas, [pos[0] + c * 72, pos[1]])
            
        pass	# draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for i in SUITS:
            for j in RANKS:
                self.deck.append(Card(i, j))
        
        pass	# create a Deck object

    def shuffle(self):
        random.shuffle(self.deck)
        # shuffle the deck 
        pass    # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()
        pass	# deal a card object from the deck
    
    def __str__(self):
        s = " "
        for i in range(len(self.deck)):
            s += str(self.deck[i]) + " "
            
        return "Deck contains " + s
        pass	# return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, score

    # your code goes here
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    
    deck.shuffle()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    print player_hand
    print dealer_hand
    outcome = "Hit or stand?"
    
    in_play = True
    if in_play:
        outcome = "You lose"
        score -= 1

def hit():
    global outcome, in_play, deck, player_hand, dealer_hand, score
    player_hand.add_card(deck.deal_card())
    
    if in_play:
        if player_hand.get_value() > 21:
            outcome = "You lose"
            in_play = False
            score -= 1
        elif player_hand.get_value == 21:
            outcome = "You win"
            in_play = False
            score += 1
        else:
            outcome = "Hit or stand?"

    
    
    

    pass	# replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, deck, player_hand, dealer_hand, score
    in_play = False
    if player_hand.get_value() > 21:
        outcome = "You busted. You lose!"
        score -= 1
    else:
        
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            outcome = "Dealer busted. You win!"
            score += 1
    
        elif dealer_hand.get_value() < 21:
            if player_hand.get_value() > dealer_hand.get_value():
                outcome = "You win! New deal?"
                score += 1
            elif player_hand.get_value() < dealer_hand.get_value():
                outcome = "You lose! New deal?"
                score -= 1
            elif player_hand.get_value() == dealer_hand.get_value():
                outcome = "You lose! New deal?"
                score -= 1
            
        
   
    pass	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    player_hand.draw(canvas,[100,300])
    dealer_hand.draw(canvas,[100,100])

    if in_play:    
        canvas.draw_image(card_back,CARD_BACK_CENTER, CARD_BACK_SIZE, [100+36,100+48], CARD_BACK_SIZE)

    canvas.draw_text("Blackjack", [100, 50], 50 ,"black")    
    canvas.draw_text(outcome,[200,250],25,'black')   
    canvas.draw_text('Score:'+ str(score),[400,80],50,'black')

    
    
                          


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

