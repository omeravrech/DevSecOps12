import hangingman
import random
from time import time_ns

def specific_chooice():
    ''' This function handle the option to choose a sentence by the user '''
    print("Please choose one of this sentences:")
    for i, sentence in enumerate(hangingman.SENTENCES_LIST):
        print(f"{i+1}. {' '.join(sentence)}")
    
    while True:
        choice = input("Enter your choice : ")
        try:
            choice = int(choice) -1
            print(f"Choice = {choice}")
            if choice < 0 or choice > len(hangingman.SENTENCES_LIST):
                raise OverflowError()
            break
        except:
            print("Please enter valid number")

    return hangingman.SENTENCES_LIST[choice]

choices = [
    {
        "description": "Exit",
        "function": exit
    },
    {
        "description" : "Random chooice",
        "function": lambda: random.choice(hangingman.SENTENCES_LIST)
    },
    {
        "description" : "Choose your sentence",
        "function" : specific_chooice
    }
]

score = 0

print("Welcome to Hanging Man game!\n")
while True:
    print("In order to start, please choose from the list below:")
    for i, choice in enumerate(choices):
        print(f"{(i)}. {choice['description']}")

    user_choice = input("Enter your chooice: ")
    if user_choice.isdigit() and 0 <= int(user_choice) < len(choices):
        func = choices[int(user_choice)]["function"]
        start_time = time_ns()
        _score = hangingman.game_round(func())
        if _score != None:
            if (time_ns() - start_time)//(10**9) <= 30:
                _score += 100
            score += _score
        print(f"You get {_score} points from this game. You have {score} points in total")
    else:
        print("Invalid input!")


