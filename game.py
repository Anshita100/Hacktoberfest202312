import random

def play_game():
    choices = ['rock', 'paper', 'scissors']

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors), or 'q' to quit: ").lower()

        if player_choice == 'q':
            print("Thanks for playing. Goodbye!")
            break

        if player_choice not in choices:
            print("Invalid choice. Please choose again.")
            continue

        computer_choice = random.choice(choices)

        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
