###############################################################################
#set up game and display rules and game board
#prompt for a command input and establish main game loop
#check if leading characters of command are 'tf' and calls tableau_to_
#foundation() if command is valid
#check if leading characters of command are 'tt' and calls tableau_to_
#tableau() if command is valid
#check if leading characters of command are 'wf' and calls waste_to_
#foundation() if command is valid
#check if leading characters of command are 'wt' and calls waste_to_tableau()
#if command is valid
#check if leading characters of command are 'sw' and calls stock_to_waste()
#if command is valid
#check if leading character of command is 'r' and re-establishes the game board
#and prints the rules if command is valid
#check if leading characters of command are 'h' and prints the rules and game
#board if command is valid
#any RuntimeErrors are delivered to be printed and the main game loop to repeat
#if is_winner() returns True, the game terminates itself and displays a victory
#banner
#if is_winner() returns False, the main game loop repeats
###############################################################################

import cards #this is required

YAY_BANNER = """
__   __             __        ___                       _ _ _ 
\ \ / /_ _ _   _    \ \      / (_)_ __  _ __   ___ _ __| | | |
 \ V / _` | | | |    \ \ /\ / /| | '_ \| '_ \ / _ \ '__| | | |
  | | (_| | |_| |_    \ V  V / | | | | | | | |  __/ |  |_|_|_|
  |_|\__,_|\__, ( )    \_/\_/  |_|_| |_|_| |_|\___|_|  (_|_|_)
           |___/|/                                            

"""

RULES = """
    *------------------------------------------------------*
    *-------------* Thumb and Pouch Solitaire *------------*
    *------------------------------------------------------*
    Foundation: Columns are numbered 1, 2, ..., 4; built 
                up by rank and by suit from Ace to King. 
                You can't move any card from foundation, 
                you can just put in.

    Tableau:    Columns are numbered 1, 2, 3, ..., 7; built 
                down by rank only, but cards can't be laid on 
                one another if they are from the same suit. 
                You can move one or more faced-up cards from 
                one tableau to another. An empty spot can be 
                filled with any card(s) from any tableau or 
                the top card from the waste.
     
     To win, all cards must be in the Foundation.
"""

MENU = """
Game commands:
    TF x y     Move card from Tableau column x to Foundation y.
    TT x y n   Move pile of length n >= 1 from Tableau column x 
                to Tableau column y.
    WF x       Move the top card from the waste to Foundation x                
    WT x       Move the top card from the waste to Tableau column x        
    SW         Draw one card from Stock to Waste
    R          Restart the game with a re-shuffle.
    H          Display this menu of choices
    Q          Quit the game
"""

def valid_fnd_move(src_card, dest_card):
    """
        determines if moving a card into the foundation is valid
        src_card: the card being moved
        dest_card: the high-card in the destination in the foundation
    """
    #if they are the same card, something really weird happend
    if src_card == dest_card:
        raise RuntimeError("Error: Invaid move")
    
    if dest_card == "":
        #if the fnd is empty and the sorce is an ace, the move is valid
        if src_card.rank() == 1:
            return True
        else: #otherwise if the sorce is any other rank, the move is invalid
            raise RuntimeError("Error: Invaid move")
        
    if src_card.rank() == dest_card.rank()+1 and src_card.suit() == \
    dest_card.suit():
        return True
    #if the conditions being passed into here cant reach a conclusion by this 
    #point, it must be invalid
    else:
        raise RuntimeError("Error: invalid move due to mismatched cards")
        
        
def valid_tab_move(src_card, dest_card):
    """
        determines if moving a card into the tableau is valid
        src_card: the card being moved
        dest_card: the high-card in the destination in the tableau
    """     
    if src_card == "": #if the sorce is empty, theres no card to be moved
        raise RuntimeError("Error: insufficient number of cards to move")
    #if they are the same card, something really weird happend
    if src_card == dest_card: 
        raise RuntimeError("Error: Invaid move")
    if dest_card == "": #if the destination is empty, any card can go there
        return True
    if src_card.rank() == dest_card.rank()-1 and src_card.suit() != \
    dest_card.suit():
        return True
    #if the conditions being passed into here cant reach a conclusion by this 
    #point, it must be invalid
    else: 
        raise RuntimeError("Error: invalid move due to mismatched cards")
            
            
def tableau_to_foundation(tab, fnd):
    """
        handles checking the validity of a move from tableau to foundation and 
        carrying out of said move
        tab: an individual column of the tableau
        fnd: an individual column of the foundation
    """
    target_card = ""
    dest_card = ""
    if len(tab) != 0: #if tab is empty here, move cannot happen
        target_card = tab[-1]
    #if fnd is empty, the element at -1 cant be called, but the move could
    #still be good
    if len(fnd) != 0:
        dest_card = fnd[-1]   
    valid_move = valid_fnd_move(target_card, dest_card)
    if valid_move == True:
        card_in_motion = tab.pop()
        fnd.append(card_in_motion)
        if len(tab) != 0: #if tab is empty, no need to flip any cards
            tab[-1].flip_card()
    
            

def tableau_to_tableau(tab1, tab2, n):
    """
        handles checking the validity of a move from one tableau to another and 
        carrying out of said move
        tab1: an individual column of the tableau
        tab2: a diffrent individual column of the tableau
        n: the number of cards from the first tableau that will be moved to the
        second
    """ 
    target_card = ""
    dest_card = ""
    if len(tab1) != 0: #if tab is empty here, move cannot happen
        dest_card = tab1[-1]
    #if tab is empty, the element at -1 cant be called, but the move could
    #still be good
    if len(tab2) >= n:
        target_card = tab2[-n]
        if target_card.is_face_up() == False:
            raise RuntimeError("Error: insufficient number of cards to move")
    else:
        raise RuntimeError("Error: insufficient number of cards to move")
    valid_move = valid_tab_move(target_card, dest_card)
    if valid_move == True:
        cycle = 0
        to_append = []
        while cycle < n:
            to_append.append(tab2.pop())
            cycle += 1
        to_append = to_append[::-1]
        if len(tab2) != 0:
            tab2[-1].flip_card()
        for card in to_append:
            tab1.append(card)
    

def waste_to_foundation(waste, fnd, stock):
    """
        handles checking the validity of a move from waste to foundation and 
        carrying out of said move
        waste: the list of cards in waste
        fnd: an individual column of the foundation
        stock: the list of cards in stock
    """    
    target_card = ""
    dest_card = ""
    if len(waste) != 0: #if waste is empty, move cannot happen
        target_card = waste[-1]
    #if fnd is empty, the element at -1 cant be called, but the move could
    #still be good
    if len(fnd) != 0:
        dest_card = fnd[-1]
    valid_move = valid_fnd_move(target_card, dest_card)
    
    if valid_move == True:
        fnd.append(waste[-1])
        waste.pop()
    

def waste_to_tableau(waste, tab, stock):
    """
        handles checking the validity of a move from waste to tableau and 
        carrying out of said move
        waste: the list of cards in waste
        tab: an individual column of the tableau
        stock: the list of cards in stock
    """    
    target_card = ""
    dest_card = ""
    if len(waste) != 0: #if waste is empty, move cannot happen
        target_card = waste[-1]     
    #if tab is empty, the element at -1 cant be called, but the move is still
    #good
    if len(tab) != 0: 
        dest_card = tab[-1]
    valid_move = valid_tab_move(target_card, dest_card)
    
    if valid_move == True:
        tab.append(waste[-1])
        waste.pop()
                    
def stock_to_waste(stock, waste):
    """
        handles checking the validity of a move from stock to waste and 
        carrying out of said move
        waste: the list of cards in waste
        stock: the list of cards in stock
    """    
    if len(stock) != 0: #if stock is empty, the move is not valid
        waste.append(stock.deal())
    else:
        print("Error: invalid move")
    
    
                            
def is_winner(foundation):
    """
        Determines if the user has won based on if the whole deck has been fit
        into the foundation
        foundation: the lists of each suit organized according to rank
    """
    if len(foundation[0])+len(foundation[1])+len(foundation[2])+\
    len(foundation[3]) == 52: 
        #if the whole deck is contained in foundation, game is complete
        print(YAY_BANNER)
        return True
    else:
        return False

def setup_game():
    """
        The game setup function, it has 4 foundation piles, 7 tableau piles, 
        1 stock and 1 waste pile. All of them are currently empty. This 
        function populates the tableau and the stock pile from a standard 
        card deck. 

        7 Tableau: There will be one card in the first pile, two cards in the 
        second, three in the third, and so on. The top card in each pile is 
        dealt face up, all others are face down. Total 28 cards.

        Stock: All the cards left on the deck (52 - 28 = 24 cards) will go 
        into the stock pile. 

        Waste: Initially, the top card from the stock will be moved into the 
        waste for play. Therefore, the waste will have 1 card and the stock 
        will be left with 23 cards at the initial set-up.

        This function will return a tuple: (foundation, tableau, stock, waste)
    """
    # you must use this deck for the entire game.
    # the stock works best as a 'deck' so initialize it as a 'deck'
    stock = cards.Deck()
    stock.shuffle()
    # the game piles are here, you must use these.
    foundation = [[], [], [], []]           # list of 4 lists
    tableau = [[], [], [], [], [], [], []]  # list of 7 lists
    waste = []                              # one list
    
    while len(stock) > 24:
        column_counter = 0
        while column_counter < 7:
            if len(tableau[column_counter]) < column_counter+1:
                top_deck = stock.deal()
                #every card should be flipped face-down while dealing the tab
                top_deck.flip_card()
                tableau[column_counter].append(top_deck)
            column_counter += 1
    #the last card in each column of the tab must be un-flipped
    for lists in tableau:
        top_card = lists.pop()
        top_card.flip_card()
        lists.append(top_card)
    
    #establishing the board includes putting the top card from stock into waste
    waste.append(stock.deal())
    
    return foundation, tableau, stock, waste


def display_game(foundation, tableau, stock, waste):
    """
        Displays the gameboard in desired format
        foundation: the foundation element of the board
        tableau: the tableau element of the board
        stock: the stock element of the board
        waste: the waste element of the board
    """
    f1, f2, f3, f4 = "", "", "", ""
    try:
        f1 = foundation[0][-1].__str__()
        f2 = foundation[1][-1].__str__()
        f3 = foundation[2][-1].__str__()
        f4 = foundation[3][-1].__str__()
    except:
        pass
    
    print("================= FOUNDATION =================")
    print("f1        f2        f3        f4        ")
    print("[{:<3}]     [{:<3}]     [{:<3}]     [{:<3}]     ".format(f1, f2, \
    f3, f4))
    print("==================  TABLEAU  =================")
    print("t1     t2     t3     t4     t5     t6     t7    ") 
    row = 0
    largest_tab = 0
    for coulumn_number, columns in enumerate(tableau):
        if len(columns) != 0:
            if columns[-1].is_face_up() == False:
                tableau[coulumn_number][-1].flip_card()
    for columns in tableau:
            if len(columns) > largest_tab:
                largest_tab = len(columns)
    while row < largest_tab:
        column_counter = 0
        while column_counter < 7:
            try:
                card = tableau[column_counter][row].__str__()
                print("{:<7}".format(card), end="")
            except:
                print("       ", end="")
            column_counter += 1
        row += 1
        print("")
    print("================= STOCK/WASTE =================")
    print("Stock #({}) ==> {}".format(len(stock),waste))


print(RULES)
fnd, tab, stock, waste = setup_game()
display_game(fnd, tab, stock, waste)
print(MENU)

command = input("prompt :> ")
while command.lower() != 'q' or command[0].lower() != 'q':
    
    try:
        command_error = False
        
        if command == "":
            raise RuntimeError("Error: no command entered")
            
        elif command[:2].lower() == "tf": #decodes a tab to fnd move
            if command[3:4] == '' or command[5:6] == '' or len(command) > 6:
                raise RuntimeError("Error: wrong number of arguments")
            try:
                pass_tab = tab[int(command[3:4])-1]
                pass_fnd = fnd[int(command[5:6])-1]
            except:
                error_msg = "Error: arguments must be numbers in range"
                raise RuntimeError(error_msg)
            tableau_to_foundation(pass_tab, pass_fnd)
        
        elif command[:2].lower() == "tt": #decodes a tab to tab move
            if command[3:4] == '' or command[5:6] == '' or command[7:8] == '' \
            or len(command) > 8:
                raise RuntimeError("Error: wrong number of arguments")
            try:
                pass_tab2 = tab[int(command[3:4])-1]
                pass_tab1 = tab[int(command[5:6])-1]
                number = int(command[7:8])
            except:
                error_msg = "Error: arguments must be numbers in range"
                raise RuntimeError(error_msg)
            tableau_to_tableau(pass_tab1, pass_tab2, number)
            
        elif command[:2].lower() == "wf": #decodes a waste to fnd move
            if command[3:4] == '' or len(command) > 4:
                raise RuntimeError("Error: wrong number of arguments")
            try:
                pass_fnd = fnd[int(command[3:4])-1]
            except:
                error_msg = "Error: arguments must be numbers in range"
                raise RuntimeError(error_msg)
            waste_to_foundation(waste, pass_fnd, stock)
        
        elif command[:2].lower() == "wt": #decodes a waste to tab move
            if command[3:4] == '' or len(command) > 4:
                raise RuntimeError("Error: wrong number of arguments")
            try:
                pass_tab = tab[int(command[3:4])-1]
            except:
                error_msg = "Error: arguments must be numbers in range"
                raise RuntimeError(error_msg)
            waste_to_tableau(waste, pass_tab, stock)
            
        elif command[:2].lower() == "sw": #decodes a stock to waste move
            if len(command) > 2:
                raise RuntimeError("Error: wrong number of arguments")
            stock_to_waste(stock, waste)
        
        elif command[:1].lower() == "r": #decodes a call to reset
            if len(command) > 1:
                raise RuntimeError("Error: wrong number of arguments")
            fnd, tab, stock, waste = setup_game()
            print(MENU)
        
        elif command[:1].lower() == "h": #decodes a call for menu
            if len(command) > 1:
                raise RuntimeError("Error: wrong number of arguments")
            print(MENU)
            
        else:
            error_msg = command + " is an Invalid Command"
            raise RuntimeError(error_msg)
        
        display_game(fnd, tab, stock, waste)
            
    except RuntimeError as error_message:#any RuntimeError raised lands here
        print("{:s}\nTry again.".format(str(error_message)))       
    
    if is_winner(fnd) != True:
        command = input("prompt :> ")
    else:
        command = "q"


#Questions
#Q1: 7
#Q2: 1
#Q3: 1
#Q4: 7