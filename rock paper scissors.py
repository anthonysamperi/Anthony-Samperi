import random

# Function to simulate a Rock, Paper, Scissors throw
def throw_rps():
    """Simulate a throw for Rock, Paper, Scissors game, returning 'Rock', 'Paper', or 'Scissors'"""
    options = ['Rock', 'Paper', 'Scissors']
    return random.choice(options)

# Function to play a single round of Rock, Paper, Scissors
def play_round(player1_throw, player2_throw):
    """
    Determines the winner of a round of Rock, Paper, Scissors.

    Args:
    player1_throw (str): The throw of Player 1.
    player2_throw (str): The throw of Player 2.
    """
    outcomes = {
        ('Rock', 'Scissors'): 'Player 1 wins the round',
        ('Scissors', 'Rock'): 'Player 2 wins the round',
        ('Paper', 'Rock'): 'Player 1 wins the round',
        ('Rock', 'Paper'): 'Player 2 wins the round',
        ('Scissors', 'Paper'): 'Player 1 wins the round',
        ('Paper', 'Scissors'): 'Player 2 wins the round',
    }
    if player1_throw == player2_throw:
        print(f"Both players threw {player1_throw}. The round is a tie.")
    else:
        result = outcomes.get((player1_throw, player2_throw), None)
        print(f"Player 1 throws {player1_throw}, Player 2 throws {player2_throw}. {result}")
# Main function to orchestrate the Rock, Paper, Scissors game
def main():
    player1_score = 0
    player2_score = 0
    tie_score = 0

    # Ask the user for the number of rounds
    rounds = int(input("How many rounds do you want to play? "))

    for _ in range(rounds):
        player1_throw = throw_rps()
        player2_throw = throw_rps()
        if player1_throw == player2_throw:
            tie_score += 1
        elif player1_throw == 'Rock' and player2_throw == 'Scissors' or \
             player1_throw == 'Scissors' and player2_throw == 'Paper' or \
             player1_throw == 'Paper' and player2_throw == 'Rock':
            player1_score += 1
        else:
            player2_score += 1

        play_round(player1_throw, player2_throw)

    # Print the final results
    print(f"\nFinal Score: Player 1 wins {player1_score} round(s). Player 2 wins {player2_score} round(s). {tie_score} round(s) ended in a tie.")
    if player1_score > player2_score:
        print("Overall Winner: Player 1!")
    elif player2_score > player1_score:
        print("Overall Winner: Player 2!")
    else:
        print("The game ends in a tie!")

if __name__ == "__main__":
    main()