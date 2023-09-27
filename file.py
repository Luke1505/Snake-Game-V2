import json
from operator import itemgetter

# Save the highscores


def save(highscores):
    with open('scoreboard.json', 'w') as file:
        # save highscores to json file and format it nicely like this [name, score],\n[name, score] etc.
        json.dump(highscores, file, indent=4)


# Load the highscores


def loadscore():
    try:
        with open('scoreboard.json', 'r') as file:
            highscores = json.load(file)  # Read the json file.
    except FileNotFoundError:
        highscores = []  # Define an empty list if the file doesn't exist.
    # Sorted by the score.
    return sorted(highscores, key=itemgetter(1), reverse=True)