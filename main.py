import random
from art import logo


    

    
def process_card():
    # returns a random card
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

# calculate score
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

# compare user score and computer score
def compare_score(user_score,pc_score):
    if user_score>21 and pc_score>21:
        return "You went over. Game Over."
    
    if user_score==pc_score:
        return "Draw"
    elif user_score==0:
        return "Black Jack! You Win!"
    elif pc_score==0:
        return "You lose. PC won the game"
    elif pc_score>21:
        return "PC went over. You win."
    elif user_score>21:
        return "You went over. Game Over."
    elif user_score>pc_score:
        return "You win!"
    else:
        return "You lose."

def run():
    print(logo)
    
    pc_cards=[]
    user_cards=[]
    is_game_over=False
    
    for _ in range(2):
        pc_cards.append(process_card())
        user_cards.append(process_card())
        
    while not is_game_over:
        pc_score=calculate_score(pc_cards)
        user_score=calculate_score(user_cards)
        
        print(f"PC's first card is: {pc_cards[0]}")
        print(f"Your cards: {user_cards}, Your current socre is: {user_score}.")
        
        if pc_score==0 or user_score==0 or user_score>21:
            is_game_over=True
        else:
            should_continue=input("Type 'y' to get a new card. Type 'n' to pass: ")
            if should_continue=="y" or should_continue=="Y":
                user_cards.append(process_card())
            elif should_continue=="n" or should_continue=="N":
                is_game_over=True
            
    while pc_score!=0 and pc_score<17:
        pc_cards.append(process_card())
        pc_score=calculate_score(pc_cards)
        
    print(f" PC's final cards: {pc_cards}; Your final score is: {pc_score}")
    print(f" Your final cards: {user_cards}; Your final score is: {user_score}")
    print(compare_score(pc_score,user_score))
    
# initialize game
while input("Start Game? Type 'y' to start the game or 'n' to ignore: ")=="y":
    run()