import random
import os

def clear_screen():
    # Clears the terminal so the menu stays at the top
    os.system('cls' if os.name == 'nt' else 'clear')

#GAME FUNCTIONS

def dice_roll():
    while True:
        clear_screen()
        print("==============================")
        print("      DICE ROLL SETTINGS      ")
        print("==============================\n")
        
        input("Press Enter to roll the dice...")
        
        number = random.randint(1, 6)
        print(f"\n[!] The dice landed on: {number}")
        
        choice = input("\nRoll again? (y/n): ").lower()
        if choice != 'y':
            break

def stone_paper_scissors():
    options = ["stone", "paper", "scissors"]
    while True:
        clear_screen()
        print("==============================")
        print("    STONE PAPER SCISSORS      ")
        print("==============================\n")
        print("Options: stone | paper | scissors")
        
        user_move = input("Enter your move: ").lower()
        
        if user_move not in options:
            print("Invalid move! Please type stone, paper, or scissors.")
            input("Press Enter to try again...")
            continue
            
        comp_move = random.choice(options)
        print(f"\nYour move: {user_move}")
        print(f"Computer:  {comp_move}")
        print("-" * 20)
        
        # Win/Loss Logic
        if user_move == comp_move:
            print("RESULT: It's a draw!")
        elif (user_move == "stone" and comp_move == "scissors") or \
             (user_move == "paper" and comp_move == "stone") or \
             (user_move == "scissors" and comp_move == "paper"):
            print(f"RESULT: You Win! {user_move.capitalize()} beats {comp_move}.")
        else:
            print(f"RESULT: You Lose! {comp_move.capitalize()} beats {user_move}.")
            
        choice = input("\nPlay another round? (y/n): ").lower()
        if choice != 'y':
            break

#  MAIN HUB LOOP 

while True:
    clear_screen()
    print("******************************")
    print("          GAME HUB            ")
    print("******************************")
    print("1. Dice Roll")
    print("2. Stone Paper Scissors")
    print("3. Exit")
    print("******************************")
    
    user_input = input("\nSelect a game (1-3): ")
    
    if user_input == "1":
        dice_roll()
    elif user_input == "2":
        stone_paper_scissors()
    elif user_input == "3":
        print("\nExiting GAME HUB... Goodbye!")
        break
    else:
        print("\nError: Please enter 1, 2, or 3.")
        input("Press Enter to continue...")
