player1 = input("Enter the name of player 1: ")
player2 = input("Enter the name of player 2: ")

play = 'y'
while play == 'y':
    choice1 = input("Enter the choice for " + player1 + ": ").lower()
    choice2 = input("Enter the choice for " + player2 + ": ").lower()
    
    if choice1 == choice2:
        print("It's a tie.")
    elif choice1 == "rock":
        if choice2 == "paper":
            print(player2 + " won")
        else:
            print(player1 + " won")
    elif choice1 == "paper":
        if choice2 == "rock":
            print(player1 + " won")
        else:
            print(player2 + " won")
    else:
        if choice2 == "paper":
            print(player1 + " won")
        else:
            print(player2 + " won")

    play = input("Do you want to play again? (y/n): ") 