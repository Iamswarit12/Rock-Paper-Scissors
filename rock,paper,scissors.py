import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")

    possible_actions = ["rock","paper","scissors"]

    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose{computer_action}.\n")     

    if user_action == computer_action:
        print(f"Both players setected{user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print(" You win!")
        else:
            print("You lose!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("You win!")
        else:
            print(" You lose!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("You win!")
        else:
            print("You lose!")
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break