import random

# Separator function to provide separation in console between plays
def separator():
    print("\n* - * - * - * - *\n")

# Function to simulate the football kickoff
def kickoff(kicking_team, receiving_team):
    separator()
    kickoff_yards = random.randint(55, 70)
    return_yards = random.randint(10, 25)
    if (kickoff_yards >= 65):
        starting_yardline = 25
        print(f"The ball was kicked by {kicking_team} for {kickoff_yards} yards to the endzone resulting in a touchback.\nThe ball is now on the {starting_yardline} yardline.\n{receiving_team} has the ball.")
    else:
        starting_yardline = 65 - (kickoff_yards - return_yards)
        print(f"The ball was kicked for {kickoff_yards} yards and returned for {return_yards} yards.\nThe ball is now on the {starting_yardline} yardline.")
    separator()

# Function to select the opponent from a list of teams
def select_opponent():
    possible_opponents = ['Dallas Cowboys', 'Chicago Bears', 'Green Bay Packers', 'Miami Dolphins', 'Los Angeles Rams', 'New York Jets']
    random_index = random.randint(0, (len(possible_opponents) - 1))
    return possible_opponents[random_index]

# Function to welcome the player and select teams
def begin_game():
    opponent = select_opponent()
    print("\n* * * Welcome to pyFootball! * * *\nA text-based football game coded in Python by Aaron McCollum.")
    user_team = input("\nWhat is the name of your team? ")
    print(f"\nToday's NFL game will be between the {user_team} and the {opponent}.")