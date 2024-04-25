import random
from replit import clear
from art import logo

def dealcard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    
    
    return sum(cards)
def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw☹️"
    elif comp_score == 0:
        return "Lose, opponent has a blackjack😱"
    elif user_score == 0:
        return 'Win with a blackjack😄😱'
    elif user_score > 21:
        return "You went over. You lose!😢"
    elif comp_score > 21:
        return "Opponent went over. You win!😀"
    elif user_score > comp_score:
        return "You win!!😄"
    else:
        return "You lose😞"
def playgame():
    user_cards = []
    comp_cards = []
    game_over = False
    for _ in range(2):
        dealcard()
        user_cards.append(dealcard())
        comp_cards.append(dealcard())

    while not game_over:  
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(dealcard())
            else:
                game_over = True
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(dealcard())
        comp_score = calculate_score(comp_cards)

    print(f"Your final hand: {user_cards}, Final Score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, Final Score: {comp_score}")
    print(compare(user_score=user_score, comp_score=comp_score))
while input("Do you want to play the game of blackjack? type 'y' or 'n'") == 'y':
    clear()
    print(logo)
    playgame()
    

    
    
    


        