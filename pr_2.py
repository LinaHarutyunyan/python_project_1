import random

print("Welcome to the Game of Craps!")

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total_sum = die1 + die2

print(f"First roll: {die1} and {die2} (Total: {total_sum})")

# First roll
if total_sum == 7 or total_sum == 11:
  print("Congratulations you won!")

elif total_sum == 2 or total_sum == 3 or total_sum == 12:
  print("Craps! The casino wins.")

else:
  goal = total_sum
  print(f"Your goal number is set to: {goal}")
  print("Keep rolling until you hit your goal again")


  while True:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total_sum = die1 + die2

    print(f"Rolled: {die1} and {die2} (Total: {total_sum})")

    if total_sum == goal:
      print("You've hit your goal")
      break
      
    elif total_sum == 7:
      print("You rolled a 7 before hitting your goal. You lose!")
      break
