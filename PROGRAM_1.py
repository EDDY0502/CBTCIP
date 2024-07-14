import random

def get_hint(secret, guess):
    correct_positions = sum(1 for s, g in zip(secret, guess) if s == g)
    correct_numbers = sum(min(secret.count(d), guess.count(d)) for d in set(secret)) - correct_positions
    return correct_positions, correct_numbers

def play_game():
    # Player 1 sets the number
    secret_number = input("Player 1, enter the multi-digit number: ")
    
    attempts_p2 = 0
    while True:
        # Player 2 guesses
        guess = input("Player 2, enter your guess: ")
        attempts_p2 += 1
        if guess == secret_number:
            print(f"Player 2 guessed correctly in {attempts_p2} attempts! Player 2 wins this round.")
            break
        else:
            correct_positions, correct_numbers = get_hint(secret_number, guess)
            print(f"Correct digits in correct positions: {correct_positions}")
            print(f"Correct digits in wrong positions: {correct_numbers}")

    # Player 2 sets the number
    secret_number = input("Player 2, enter the multi-digit number: ")

    attempts_p1 = 0
    while True:
        # Player 1 guesses
        guess = input("Player 1, enter your guess: ")
        attempts_p1 += 1
        if guess == secret_number:
            print(f"Player 1 guessed correctly in {attempts_p1} attempts! Player 1 wins this round.")
            break
        else:
            correct_positions, correct_numbers = get_hint(secret_number, guess)
            print(f"Correct digits in correct positions: {correct_positions}")
            print(f"Correct digits in wrong positions: {correct_numbers}")

    # Determine the winner
    if attempts_p1 < attempts_p2:
        print("Player 1 is crowned Mastermind!")
    else:
        print("Player 2 is crowned Mastermind!")

if __name__ == "__main__":
    play_game()
