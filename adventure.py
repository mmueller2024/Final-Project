import random

def death_message():
    message = random.randint(1, 10)
    if message == 1:
        print("you didnt have to die")
    if message == 2:
        print("lol")
    if message == 3:
        print("it's just a scratch...")
    if message == 4:
        print("game over ¯\_(ツ)_/¯")
    if message == 5:
        print("sucker")
    if message == 6:
        print("get good")
    if message == 7:
        print("have a nice death")
    if message == 8:
        print("just imagine the hospital bill...")
    if message == 9:
        print("your mother wouldn't have supported that decision.")
    if message == 10:
        print("lol")

def adventure_game():
    print("")
    print("Welcome to the Adventure Game!")
    print("What do you want to name your character?")
    print("")
    character_name = input()
    print("")
    print("Great! " + character_name + " is a person living in a small village.")
    print("One morning, " + character_name + " wakes up and notices that their little brother named Microwave is missing!")
    print(character_name + " must save Microwave!")
    print("First, do you want to try the forest or the beach?")
    print("")
    print("input forest for forest and beach for beach")
    print("")
    forest_or_beach = input()
    print("")
    if forest_or_beach == "beach":
        print("")
        print("On the beach, you find a rickety little dinghy. Do you want to go in it, or look for something else?")
        print("input 'yes' for dingy or 'no' for something else")
        print("")
        dinghy_or_forest = input()
        if dinghy_or_forest == "yes":
            print("")
            print("You get in the dinghy.")
            print("Unfortunately, the boat in unseaworthy and it starts to leak in a major way offshore.")
            print("However, you see an island off in the distance. Do you try to make it?")
            print("Input 'yes' or 'no'")
            swim_and_drown_1 = input()
            if swim_and_drown_1 == "yes":
                print("")
                drown_chances = random.randint(1, 5)
                if drown_chances == 2:
                    print("You drown before you make it to the island.")
                    print("You die.")
                    print("")
                    print("Achievement Unlocked: 'Fishfood'")
                    print("")
                    # ADD ACHIEVEMENT DICTIONARY
                else:
                    print("You make it to the island.")
                    print("However, there are a lot of crabs...")
                    print("They all start attacking you.")
                    print("")
                    print("You get eaten alive by coconut crabs on the beach.")
                    print("")
                    print("Achievement Unlocked: 'Amelia Earhart'")
                    print("")
                    # ADD ACHIEVEMENT DICTIOANRY
            if swim_and_drown_1 == "no":
                print("")
        if dinghy_or_forest == "no":
            print("")
            print("You look around for something else.")
            print("...")
            print("All of a sudden, a bunch of crabs run toward you! Do you want to run or hide?")
            print("Input 'run' to run or 'hide' to hide")
            print("")
            run_or_hide_crabs = input()
            if run_or_hide_crabs == "run":
                print("")
                print("Even though " + character_name + " tries to run, they arent able to outrun the beach crabs.")
                print("")
                print("You die by getting eaten alive by crabs.")
                print("")
                death_message()
            if run_or_hide_crabs == "hide":
                print("")
    if forest_or_beach == "forest":
        print("")
        print(character_name + " chose to go to the forest.")



adventure_game()
