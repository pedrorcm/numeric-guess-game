from random import randint
from tokenize import Number

# Defines the game difficulty, or exit game.
def difficulty():
    diff = int(input("Choose a difficulty:\n1.Easy\n2.Normal\n3.Hard\n4.Exit\n> "))
    if diff == 1:
        attempts = 7
    elif diff == 2:
        attempts = 5
    elif diff == 3:
        attempts = 3
    elif diff == 4:
        exit()
    else:
        print("Enter a valid difficulty\n")
        attempts = difficulty()

    return attempts

# Defines the secret number
def secret_number():
    number = randint(0, 100)
    return number

# Tests if the guess is valid, then if its right or wrong
def guess_tester(guess, number, rounds):
    if guess < 0 or guess > 100:
        print("\nMake a valid guess\n")
        return False
    else:
        if guess == number:
            right_answer(rounds)
        elif guess < number:
            print("\nNope. Try a higher value.")
            return True
        else:
            print("\nNope. Try a lower value.")
            return True

# Sequence if player wins
def right_answer(rounds):
    total_points = points(rounds)
    print('''
Congratulations!! That's the RIGHT ANSWER!!! yayyy!!!
        Your total score was: {:.2f}\n\n'''.format(total_points))
    write_on_leaderboard(total_points)
    play(difficulty())
# Sequence if players loses
def game_over(number):
    print(
        f"\n@@@ GAME OVER. You exausted your chances, the secret number was {number}!@@@\n\n")
    play(difficulty())

# Calculate a number of points with a simple formula
def points(rounds):
    initial_points = 100
    total_points = initial_points - (rounds*10.1)
    return total_points

# Write (Or creates if inexistent) a .txt file with the winners names and scores
def write_on_leaderboard(total_points):
    player_name = input("Enter your name: ")
    file = open("guess_game_leaderboards.txt", "a")
    file.write("\n{} - {:.2f}".format(player_name, total_points))
    print("Your name has been written in the Leaderboards. \n")
    file.close()

# Main function, makes a loop while the player still has chances. Counts rounds, and increases if guesses are wrong.
def play(attempts):
    number = secret_number()
    rounds = 0

    while rounds < attempts:
        print(f"Round {rounds+1} of {attempts}")
        guess = int(input("Make a guess (0-100): "))

        if guess_tester(guess, number, rounds):
            rounds += 1
            points(rounds)

    game_over(number)

if __name__=='__main__':
    play(difficulty())