import random
from art import logo,vs
from game_data import data

# display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:
    def format_data(account):
        """Format the account data into printable format"""
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]
        return f"{account_name},{account_descr},{account_country}"

    def check_answer(user_guess,a_followers, b_followers):
        """Take users guess and the follower counts and returns if they got it right"""
        if a_followers > b_followers:
            return user_guess == "a"
        else:
            return user_guess == "b"

    # generate random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")


    # Ask user for a guess
    guess = input("Who has more followers? 'A' or 'B': " ).lower()

    # clear the screen
    print("\n" * 20)
    print(logo)

    # check if the user is correct
    # - get follower of each account
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower,b_follower)


    # - use if statement to check if user is correct
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False









