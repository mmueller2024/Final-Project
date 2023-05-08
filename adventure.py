import random
from time import sleep

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
    sleep(1)
    print("What do you want to name your character?")
    print("")
    character_name = input()
    print("")
    print("Great! " + character_name + " is a person living in a small village.")
    sleep(1)
    print("One morning, " + character_name + " wakes up and notices that their little brother named Microwave is missing!")
    print(character_name + " must save Microwave!")
    sleep(1)
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
            sleep(1)
            print("Unfortunately, the boat is unseaworthy and it starts to leak in a major way offshore.")
            sleep(1)
            print("However, you see an island off in the distance. Do you try to make it?")
            sleep(1)
            print("Input 'yes' or 'no'")
            swim_and_drown_1 = input()
            if swim_and_drown_1 == "yes":
                print("")
                drown_chances = random.randint(1, 5)
                if drown_chances == 2:
                    sleep(1)
                    print("You drown before you make it to the island.")
                    sleep(1)
                    print("You die.")
                    print("")
                    sleep(1)
                    print("Achievement Unlocked: 'Fishfood'")
                    print("")
                    # ADD ACHIEVEMENT DICTIONARY
                else:
                    
                    sleep(1)
                    print("You make it to the island.")
                    sleep(1)
                    print("However, there are a lot of crabs...")
                    sleep(1)
                    print("They all start attacking you.")
                    print("")
                    sleep(1)
                    print("You get eaten alive by coconut crabs on the beach.")
                    print("")
                    sleep(1)
                    print("Achievement Unlocked: 'Amelia Earhart'")
                    print("")
                    # ADD ACHIEVEMENT DICTIOANRY
            if swim_and_drown_1 == "no":
                print("")
                sleep(1)
                print("You stay in the boat")
                sleep(1)
                print("The leaks get so bad that you sink and drown.")
                sleep(1)
                print("You died")
                print("")
                sleep(1)
                death_message()
        if dinghy_or_forest == "no":
            print("")
            sleep(1)
            print("You look around for something else.")
            sleep(1)
            print("...")
            sleep(1)
            print("All of a sudden, a bunch of crabs run toward you! Do you want to run or hide?")
            sleep(1)
            print("Input 'run' to run or 'hide' to hide")
            print("")
            run_or_hide_crabs = input()
            if run_or_hide_crabs == "run":
                print("")
                sleep(1)
                print("Even though " + character_name + " tries to run, they arent able to outrun the beach crabs.")
                sleep(1)
                print("")
                print("You die by getting eaten alive by crabs.")
                sleep(1)
                print("")
                death_message()
            if run_or_hide_crabs == "hide":
                print("")
                sleep(1)
                print("You try to hide from the crabs but they have")
    if forest_or_beach == "forest":
        print("")
        print(character_name + " chose to go to the forest.")
        disco_party = random.randint(1,10)
        if disco_party ==5:
            print("")
            sleep(1)
            print("ALIENS!! OH NO!!!!")
            sleep(1)
            print("THEY ARE BLASTING YOU WITH LASERS!!!!")
            sleep(1)
            print("")
            print("You died from the alien invasion.")
            sleep(1)
            print("")
            print("Achievement Unlocked: 'Lit Disco Party'")
        else:
            print("xxxxxxxxx")



adventure_game()
