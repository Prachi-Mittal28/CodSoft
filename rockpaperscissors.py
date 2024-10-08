import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to play the game
def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        # User input
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Computer selection
        computer_choice = random.choice(choices)

        # Determine and display the result
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display scores
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")

        # Ask to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

# Main program
if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
    print("Thanks for playing!")
