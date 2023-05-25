import random
import json

from time import sleep
from first_aid import first_aid_game
from adventure import adventure_game

def main():
    print("")
    print("Hello!")
    print("Choose your game:")
    print("- Adventure Game (input 'adventure')")
    print("- First Aid Test (input 'first aid')")
    print("- See Adventure Achievements (input 'achievements')")
    print("")
    user_input = input()
    if user_input == "adventure":
        adventure_game()
    if user_input == "first aid":
        first_aid_game()
    if user_input == "achievements":
        print("")
        print("There are five possible achievements to unlock:")
        print("'Fishfood', 'Amelia Earhart', 'Lit Disco Party', 'Best Friends', 'Yummy Dinner', and 'Find Microwave'")
        print("")
        with open ("achievements.json", "r") as f:
            achievements = json.load(f)
        print(achievements)
        print("")
    else:
        print("")
        print("unknown input, try again")
        print("")

main()


