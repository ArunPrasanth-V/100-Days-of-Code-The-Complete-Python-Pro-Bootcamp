import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif user_score==0:
        return "Lose , Opponant had black jake"
    elif user_score==0:
        return "You win with black jack"
    elif user_score>21:
        return "You went over, lose "
    elif computer_score>21:
        return "Opponent went over you win !! "
    elif computer_score<user_score:
        return "You win !!"
    else:
        return "You lose"
def calculate_score(lists):
    if sum(lists)==21 and len(lists)==2:
        return 0
    if 11 in lists and sum(lists)>21:
        lists.remove(11)
        lists.append(1)
    return sum(lists)
gameOver=False
user_card=[]
computer_card=[]
for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())
user_score=calculate_score(user_card)
computer_score=calculate_score(computer_card)
while not gameOver:

    print(f"YOUR cards : {user_card} , CURRENT Score : {user_score}")
    print(f"Computer First card : {computer_card[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        gameOver = True
    else:
        user_deal = input("'y' to get another card or 'n' : ")
        if user_deal == "y":
            user_card.append(deal_card())
        else:
            gameOver = True
    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)
    print(compare(user_score,computer_score))
