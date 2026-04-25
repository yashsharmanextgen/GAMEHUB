import random

# ===================== DICE ASCII =====================
dice_art = r"""
  ____
 /\' .\    _____
/: \___\  / .  /\
\' / . / /____/..\
 \/___/  \'  '\  /
          \'__'\/
"""

# ===================== RPS ASCII =====================
rps_art = r"""
✊  ✋  ✌️
Rock Paper Scissors
"""

# ===================== DICE GAME =====================
def dice_roll():
    print(dice_art)
    print("🎲 Welcome to Dice Roll!\n")

    roll = random.randint(1, 6)
    print(f"You rolled: {roll} 🎲")


# ===================== RPS GAME =====================
def rock_paper_scissors():
    print(rps_art)
    print("\nChoose:")
    print("1 → ✊ Rock")
    print("2 → ✋ Paper")
    print("3 → ✌️ Scissors")

    user_input = input("Enter your choice (1/2/3): ")

    if user_input not in ["1", "2", "3"]:
        print("❌ Invalid choice! Please select 1, 2, or 3.")
        return

    choices = {
        "1": "✊ Rock",
        "2": "✋ Paper",
        "3": "✌️ Scissors"
    }

    user_choice = choices[user_input]
    computer_input = random.choice(["1", "2", "3"])
    computer_choice = choices[computer_input]

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    # Game logic
    if user_input == computer_input:
        print("🤝 It's a draw!")
    elif (
        (user_input == "1" and computer_input == "3") or
        (user_input == "2" and computer_input == "1") or
        (user_input == "3" and computer_input == "2")
    ):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")


# ===================== MAIN MENU =====================
def main():
    print("🎮 Welcome to Game Hub!\n")
    print("Choose a game:")
    print("1 → Dice Roll 🎲")
    print("2 → Rock Paper Scissors ✊✋✌️")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        dice_roll()
    elif choice == "2":
        rock_paper_scissors()
    else:
        print("❌ Invalid choice! Please select 1 or 2.")


# Run program
if __name__ == "__main__":
    main()