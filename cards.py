#be able to add cards to a deck until the user indicates otherwise
#- key to exit (for both adding cards and practice state?)
#two-sided card (object-oriented)
#ask user if they want to practice cards
#randomly go through the deck
#for each card, pressing space will flip to the other side
#want to be able to have an option for multi-sided cards but the user can toggle
#settings to NOT show a particular side (e.g. if I made a 3-sided card to
#practice Chinese but didn't want to show the pinyin in practice mode)

ADD_CARDS = 1
PRACTICE = 2
DONE = 3
CREATE_DECK = 4

decks = {}

#create a deck class that contains cards???
#then the deck can have its own practice method

class Card:
    def __init__(self):
        front = ""
        back = ""
        
    def set_front(self, info):
        self.front = info

    def set_back(self, info):
        self.back = info

    def get_front(self):
        return self.front

    def get_back(self):
        return self.back

    #set or list of sides on the card so we can iterate for practice mode

class Deck:
    def __init__(self, name):
        #self.name = name
        self.cards = set()
        self.name = name
        #learn about sets

    def add_card(self, card):
        (self.cards).add(card)

    def get_cards(self):
        return self.cards


def create_deck():
    #if it's a new deck, don't have to worry about printing deck
    print("creating deck")
    deck_name = input("Name of the deck: ")
    new_deck = Deck(deck_name)
    #add to dictionary of decks
    decks[deck_name] = new_deck
    #list options: add cards, edit, print, delete
    #what if there is invalid input
    next_step = input("Add cards, delete deck? ")

    while (next_step != "add cards" and next_step != "delete"):
        print("Invalid input!")
        next_step = input("Add cards, delete deck? ")

    if (next_step == "add cards"):
        add_cards(new_deck)
    elif (next_step == "delete"):
        #delete deck from set of decks
        decks.pop(deck_name)
   
        
        
def add_cards(deck):
    print("adding cards")
    done = False
    #if input is 'q' then change done to True
    while (done == False):
        #continue adding cards
        print("Front side: ")
        #create the card first then ask for front and back values
        front = input()
        if (front == "q"):
            done = True
            break
        print("Back side: ")
        back = input()
        if (back == "q"):
            done = True
            break
        new_card = Card()
        new_card.set_front(front)
        new_card.set_back(back)
        deck.add_card(new_card)

def practice(deck):
    print("practicing")
    done = False

    for card in deck.get_cards():
        #print(card.get_front())
        print(card.get_front())
        key_press = input()
        if key_press == "q":
            break
        elif key_press == "=":
            print(card.get_back())
        key_press = input() #quick fix for not going straight to the next card
        

def home():
    print("Home Page:\n")
    #show list of decks
    if len(decks) == 0:
        print("No decks created!")
    for key in decks.keys():
        print(key)
    #option to create deck
    print("1. Add cards")
    print("2. Practice")
    print("3. Quit")
    print("4. Create deck")
    mode = input("Choose next step: ")
    print(mode)
    #if user does not enter valid input

    #NOW THIS CHECK IS INVALID
    
    while (mode != "add cards" and mode != "practice" and mode != "quit" and mode != "create deck" and mode not in decks):
        print("Invalid input!")
        mode = input("Choose next step: ")
    #print(mode)
    

    #QUESTION: how to select a specific deck? would you have to iterate?
    #what if mode is the name of a deck? how to redirect?
    #first check if the input is in the decks dictionary
    #if it's in the dictionary, run through the deck method

    return mode



def main():
    print("Flash Cards")
    mode = home() #can't do int anymore
    #deck = Deck() #user should choose to create deck
    print("mode: ", mode)
    
    
    while mode != "quit":
        if (mode == "add cards"):
            print("switching modes")
            #add_cards(deck)
            
        elif (mode == "practice"):
            print("practice mode")
            #practice(deck)
        elif (mode == "create deck"):
            create_deck()
        elif (mode in decks):
            print("calling decks method")
        mode = home()
    print("Exited successfully")
    

    #testing Card class
    '''
    print("testing card class")
    card1 = Card()
    card1.set_front("bonjour")
    card1.set_back("hello")
    print(card1.get_front())
    print(card1.get_back())
    '''
    

main()