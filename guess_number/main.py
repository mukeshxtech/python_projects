import art
import random


print(art.logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check users guess against actual answer
def check_answer(user_guess,actual_answer,turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")

#Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    #choosing a random number between 1 and 100
    print("Welcome to the Number guessing game!\nI'm thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")


    turns = set_difficulty()

    #Rep
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess the number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif turns != 0:
            print("Guess again.")



game()

