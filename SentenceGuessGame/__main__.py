import functions
import random
from time import time_ns

SENTENCES_LIST = functions.load_sentences()

def specific_chooice():
    ''' This function handle the option to choose a sentence by the user '''

    print("Please choose one of this sentences (0 for exit):")
    for i, sentence in enumerate(SENTENCES_LIST):
        print(f"{i+1}. {' '.join(sentence)}")
    
    while True:
        choice = input("Enter your choice : ")
        try:
            choice = int(choice)
        except:
            choice = -1
        if choice < 0 or choice >= len(SENTENCES_LIST):
            print("Please enter valid number")
        elif choice == 0:
            return None
        else:
            return SENTENCES_LIST[choice -1]


def main():
    ''' This function is the main function of the game.
        Reponsible to handle the game type selection, sum the score,
        and run the games for the user '''
    
    # Constants
    MAIN_MENU = [ 
        {
            "description": "Exit",
            "function": exit
        },
        {
            "description" : "Random chooice",
            "function": lambda: random.choice(SENTENCES_LIST)
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
        for i, choice in enumerate(MAIN_MENU):
            print(f"{(i)}. {choice['description']}")

        user_choice = input("Enter your chooice: ")
        if user_choice.isdigit() and 0 <= int(user_choice) < len(MAIN_MENU):
            get_sentence = MAIN_MENU[int(user_choice)]["function"]
            sentence = get_sentence()
            if sentence == None:
                continue
                
            start_time = time_ns()      # Save the current timestamp for the start of this one game in nanoseconds
            one_game_score = functions.game_round(sentence)
            if one_game_score != None:
                if (time_ns() - start_time)//(10**9) <= 30: # calculate if the end time minus start time is smaller then 30 seconds 
                    one_game_score += 100
                score += one_game_score
            print(f"You get {one_game_score} points from this game. You have {score} points in total")
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()