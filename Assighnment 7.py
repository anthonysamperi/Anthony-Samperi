import random

#function to simulate rolling dice
def roll():
    options = [1, 2, 3, 4, 5, 6]
    return random.choice(options)
#function to play round
def round(player1_throw, player2_throw):
#argments to decide who wins the round
       if  player1_throw > player2_throw:
           print(f"Player 1 rolled {player1_throw}, Player 2 rolled {player2_throw}, Player 1 wins the round.")
       elif player1_throw < player2_throw:
           print(f"Player 1 rolled {player1_throw}, Player 2 rolled {player2_throw}, Player 2 wins the round.")
       else:
           print(f"Player 1 rolled {player1_throw}, Player 2 rolled {player2_throw}, The players tied this round.")
def main():
    player1_score=0
    player2_score=0
    tie_score=0
    #ask user to input number of rounds to play with error handling

    rounds=int(input("How many rounds do you want to play: "))



    print("Invalid input please input an integer")
#loop to count and keep the score
    for _ in range(rounds):
        player1_throw = roll()
        player2_throw = roll()
        if player1_throw == player2_throw:
            tie_score += 1
        elif player1_throw>player2_throw:
            player1_score+=1
        else:
            player2_score+=1

        round(player1_throw, player2_throw)
#prints out the output with the score of each player
    print(
        f"\nFinal Score: Player 1 wins {player1_score} round(s). Player 2 wins {player2_score} round(s). {tie_score} round(s) ended in a tie.")
    if player1_score > player2_score:
        print("Overall Winner: Player 1!")
    elif player2_score > player1_score:
        print("Overall Winner: Player 2!")
    else:
        print("The game ends in a tie!")


if __name__ == "__main__":
    main()

