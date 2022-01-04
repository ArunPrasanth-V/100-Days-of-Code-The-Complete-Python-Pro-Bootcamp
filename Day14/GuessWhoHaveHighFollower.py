from game_data import data
import random


def format_data(account):
    account_name = account["name"]
    account_descrip = account["description "]
    account_country = account["country"]
    return f"{account_name},a {account_descrip}, from {account_country}"


def check_answer(guess, accountA, accountB):
    if accountA > accountB:
        return guess == 'a'
    else:
        return guess == 'b'

accountB = random.choice(data)
score = 0
choice_is_right=True
while choice_is_right:
    notOut = False
    accountA = accountB
    accountB = random.choice(data)
    if accountA == accountB:
        accountB = random.choice(data)
    print("CompareA : ", format_data(accountA))
    print("\n\n        VS... \n\n")
    print("AgainstB : ", format_data(accountB))

    guess = input("Enter Your Guess A or B : ").lower()
    a_follower = accountA["Follower_count"]
    b_follower = accountB["Follower_count"]
    iscorrect = check_answer(guess,a_follower ,b_follower)
    if iscorrect:
        score+=1
        print(f"You're Correct !! currentScore : {score}.")
    else:
        choice_is_right=False
        print(f"Sorry, That Wrong. Final Score {score}.")
