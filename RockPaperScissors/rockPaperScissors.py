import random

while True:

    user_action = input("\nEnter a choice(Rock, Paper, Scissors): ")

    possible_action = ["Rock","Paper","Scissors"]
    computer_action = random.choice(possible_action)

    print("\nYou choose",user_action,",Computer chose",computer_action,"\n")

    if user_action == computer_action:
        print("Both players selected",user_action,".It's a tie \n")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("Rock smashes scissors! You win!\n")
        else:
            print("Paper covers rock! You lose!\n")
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers rock! You win!\n")
        else:
            print("Scissors cuts paper! You lose!\n")
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cuts paper! You win!\n")
        else:
            print("Rock smashes scissors! You lose!\n")

    play_again = input("Play again? (Y/N): ")
    if play_again.upper() != "Y":
        break


