[README (1).md](https://github.com/user-attachments/files/33282088/README.1.md)[Uploading# 🐍 Python Projects

My Python projects. Each project has its own section below.

## 🚀 Getting started

**Requirements:** Python 3.6 or newer. No extra libraries are needed.

```bash
git clone https://github.com/LinaHarutyunyan/python_projects_.git
cd python_projects_
```

Or click **Code → Download ZIP** on this page and unzip it.

Then follow the **How to run** step in the project you want. If `python3` is not recognized on your computer, try `python` instead.

---

## 📝 Project 1: Mad Libs

Pick a story template, type in the words the game asks for, and get a silly story back.

### How to run

```bash
python3 project_1.py
```

### Features

- Three story templates to choose from
- Prompts for nouns, adjectives, verbs, adverbs, colors, numbers and more
- A random silly word added to every story by the program
- Names are capitalized automatically
- A clear message when the template choice is invalid

### Story templates

| # | Story | Words to enter |
|---|---|---|
| 1 | 🏥 A day in the hospital | 15 |
| 2 | ⛺ A camping weekend | 12 |
| 3 | 🏰 A letter from an enchanted castle | 20 |

The random silly word is picked from `Banana`, `Noodle`, `Bloop` and `Soggy Waffle`.
Some prompts have hints, such as `(plural)`, `(ending in -ing)` or `(ending in -ly)`. Follow them for the funniest results.

### Example session

Template 2, with the answers `anna`, `backpack`, `excited`, `dancing`, `nervous`, `bear`, `sing`, `blue`, `quickly`, `3`, `hours` and `marshmallows`:

```
Welcome to Mad Libs
Select a template [1-3]: 2
You chose 2
Type a person's name: anna
Type a noun: backpack
Type an adjective(feeling): excited
Type a verb (ending in -ing): dancing
Type another adjective(feeling): nervous
Type an animal: bear
Type another verb: sing
Type a color: blue
Type an adverb (ending in -ly): quickly
Type a number: 3
Type a measure of time: hours
Type another noun: marshmallows
Here is your story:

  This weekend I am going camping with Anna. I packed my lantern, sleeping bag,
  and backpack. I am so excited to dancing in a tent. I am nervous we might see a/an bear.
  I hear they're kind of dangerous. While we're camping, we are going to hike, fish, and sing.
  I have heard that the blue lake is great for dancing. Then we will quickly hike through the forest for 3 hours.
  If I see a blue bear while hiking, I am going to bring it home as a pet!
  At night we will tell 3 Noodle stories and roast marshmallows around the campfire!!

Thanks for playing Mad Libs! 🎉
```

The silly word (`Noodle` here) is different from run to run.

### What I used

- `input()` and `print()`
- Variables and f-strings
- `if / elif / else`
- `random.choice`
- String methods such as `.title()`

---

## 🎲 Project 2: Craps

A terminal version of the classic dice game **Craps**. The program rolls two dice and decides whether you win or lose by following the rules of the game.

### How to run

```bash
python3 project_2.py
```

### How the game works

1. Roll two dice.
2. Look at the **first roll**:
   - Sum is **7 or 11** → you win.
   - Sum is **2, 3 or 12** → you lose.
   - Any other sum (**4, 5, 6, 8, 9, 10**) → that number becomes your **goal**.
3. Once a goal is set, keep rolling:
   - Roll the **goal** again → you win.
   - Roll a **7** → you lose.
   - Anything else (even an 11) → roll again.

### Example output

A game decided on the first roll:

```
Welcome to the Craps Game! (^_^)
The sum of dice is 3 + 4 = 7
Congratulations! You won the game! \(^o^)/
```

A game with a goal number:

```
Welcome to the Craps Game! (^_^)
The sum of dice is 3 + 1 = 4
Now your goal number is 4
The sum of dice is 1 + 1 = 2
The sum of dice is 1 + 5 = 6
The sum of dice is 2 + 5 = 7
Sorry! You lost the game. Better luck next time! (T_T)
```

### How the code is organized

Each function has one job, and `main()` connects them.

| Function | What it does |
|---|---|
| `roll_dice()` | Rolls two dice and returns both values |
| `show_roll(die1, die2)` | Prints one line with both dice and their sum |
| `first_roll_result(sum_dice)` | Decides whether the first roll is a win, a loss, or sets a goal |
| `play_for_goal(goal)` | Keeps rolling until the goal (win) or a 7 (lose) appears |
| `play_game()` | Plays one full game and returns the result |
| `main()` | Prints the welcome and the final message |

```
main()
└── play_game()
    ├── roll_dice()
    ├── show_roll()
    ├── first_roll_result()
    └── play_for_goal()
        ├── roll_dice()
        └── show_roll()
```

### What I used

- Functions with parameters and return values (including returning two values)
- `while` loops and `if / elif / else`
- The `random` module
- Docstrings and f-strings
 
