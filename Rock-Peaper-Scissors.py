import random
while True:
    cpuwins = 0
    userwins = 0
    print("Welcome to Rock, Paper, Scissors!")
    menu = input("Enter 'play' to play or 'quit' to exit: ")
    if menu == "play":
        print("Game Started!")
        while cpuwins < 3 and userwins < 3:
            cpuchoice = random.choice(["rock", "paper", "scissors"])
            userchoice = input("Player choice (rock, paper, scissors): ")
            if userchoice == "rock" :
                if cpuchoice == "rock":
                    print("It's a tie!")
                elif cpuchoice == "paper":
                    print("You lose this round!")
                    cpuwins += 1
                elif cpuchoice == "scissors":
                    print("You win this round!")
                    userwins += 1
                else:
                    print("Invalid choice")
            elif userchoice == "paper":
                if cpuchoice == "rock":
                    print("You win this round!")
                    userwins += 1
                elif cpuchoice == "paper":
                    print("It's a tie!")
                elif cpuchoice == "scissors":
                    print("You lose this round!")
                    cpuwins += 1
                else:
                    print("Invalid choice")
            elif userchoice == "scissors":
                if cpuchoice == "rock":
                    print("You lose this round!")
                    cpuwins += 1
                elif cpuchoice == "paper":
                    print("You win this round!")
                    userwins += 1
                elif cpuchoice == "scissors":
                    print("It's a tie!")
                else:
                    print("Invalid choice")
            print("CPU wins:", cpuwins, "User wins:", userwins)
        if cpuwins == 3:
            print("CPU wins the game!")
        elif userwins == 3:
            print("You win the game!")
    elif menu == "quit":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice")