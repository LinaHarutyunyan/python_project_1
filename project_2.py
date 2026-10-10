"""Craps: a two-dice game played in the terminal."""

import random

def roll_dice():
   """Roll two dice and return both values."""
   die1 = random.randint(1, 6)
   die2 = random.randint(1, 6)
   return die1, die2


def show_roll(die1, die2):
    """Print one line with both dice and their sum."""
    print(f"The sum of dice is {die1} + {die2} = {die1 + die2}")


def first_roll_result(sum_dice):
    """Return "win", "lose" or "goal" for the sum of the first roll."""
    if sum_dice in (7 , 11):
        return "Win!"
    elif sum_dice in (2, 3, 12):
        return "Lose!"
    else:
        return "Goal"


def play_for_goal(goal):
    """Roll until the goal appears ("win") or a 7 appears ("lose")."""
    while True:
        die1, die2 = roll_dice()
        show_roll(die1, die2)
        sum_dice = die1 + die2
        if sum_dice == goal:
            return "Win!"
        elif sum_dice == 7:
            return "Lose!"


def play_game():
    """Play one full game and return "win" or "lose"."""
    die1, die2 = roll_dice()
    show_roll(die1, die2)
    sum_dice = die1 + die2
    result = first_roll_result(sum_dice)
    if result == "Goal":
        print(f"Now your goal number is {sum_dice}")
        result = play_for_goal(sum_dice)
    return result


def main():
    """Run the game and print the final message."""
    print("Welcome to the Craps Game! (^_^)")
    result = play_game()
    if result == "Win!":
        print("Congratulations! You won the game! \\(^o^)/")
    else:
        print("Sorry! You lost the game. Better luck next time! (T_T)")


main()
