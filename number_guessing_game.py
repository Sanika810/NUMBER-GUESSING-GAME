import random

def display_title():
    """Display the game title and rules."""
    print("🎮 Number Guessing Game 🎮")
    print("Guess a number between 1 and 10 until you get it right!\n")

def play_game():
    """Core game loop where the user guesses the number."""
    number = random.randint(1, 10)
    guess = 0

    while guess != number:
        try:
            guess = int(input("Enter your guess (1-10): "))
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("🎉 You guessed it right!")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main function to run the game and allow replay."""
    display_title()
    play_again = "yes"

    while play_again.lower() == "yes":
        play_game()
        play_again = input("Do you want to play again? (yes/no): ")

    print("👋 Thanks for playing! Goodbye.")

if __name__ == "__main__":
    main()
