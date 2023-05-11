import random
from time import sleep
import json

def death_message():
    message = random.randint(1, 10)
    if message == 1:
        print("lol")
    if message == 2:
        print("lol")
    if message == 3:
        print("it's just a scratch...")
    if message == 4:
        print("game over ¯\_(ツ)_/¯")
    if message == 5:
        print("sucker lol")
    if message == 6:
        print("get good at the game")
    if message == 7:
        print("have a nice death")
    if message == 8:
        print("just imagine the hospital bill...")
    if message == 9:
        print("your mother wouldn't have supported that decision lol ")
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
                    fishfood_name = input("Please enter your name:" )
                    fishfood_dict = {
                        fishfood_name:"Fishfood"
                    }
                    with open("achievements.json", "w") as f:
                        json.dump(fishfood_dict, f)
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
                    amelia_name = input("Please enter your name: ")
                    amelia_dict = {
                        amelia_name:"Amelia Earhart"
                    }
                    with open("achievements.json", "w") as f:
                        json.dump(amelia_dict, f)
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
                print("You try to hide from the crabs but they find you anyways.")
                print("You die.")
                death_message()
    if forest_or_beach == "forest":
        print("")
        print(character_name + " chose to go to the forest.")
        disco_party = random.randint(1,10)
        if disco_party == 5:
            print("")
            sleep(1)
            print("Aliens!! Oh no!")
            sleep(1)
            print("THEY ARE BLASTING YOU WITH LASERS!!!!")
            sleep(1)
            print("")
            print("You died from the alien invasion.")
            death_message()
            sleep(1)
            print("")
            print("Achievement Unlocked: 'Lit Disco Party'")
            print("")
            disco_name = input("Please enter your name:" )
            disco_dict = {
                disco_name:"Lit Disco Party"
            }
            with open("achievements.json", "w") as f:
                json.dump(disco_dict, f)
        else:
            print("")
            sleep(1)
            print("As you walk along the path, you see a dog. Do you want to try to tame it?")
            print("Input 'yes' to tame and 'no' to leave alone.")
            print("Hint: dog can be useful later on...")
            dog_taming_input = input()
            if dog_taming_input == "yes":
                random_dog = random.randint(1,10)
                if random_dog == 5:
                    dog = 0
                else: dog = 1
            else:
                dog = 0
            print("")
            sleep(1)
            if dog == 1:
                print("You now have a dog!")
            if dog == 0:
                print("You did not tame the dog.")
            print("")
            sleep(1)
            print("There seems to be a villiage off to the side, " + character_name + " can see some smoke rising.")
            print("Do you want to check it out?")
            print("Input 'yes' to check out the villiage and 'no' to stay in the forest")
            print("")
            if dog == 1:
                print("Warning: your dog seems to be very afraid of the villiage and refuses to go near it.")
            print("")
            villiage_choice = input()
            if villiage_choice == "yes":
                print("")
                print("As you approach the villiage, you realize that a tribe of cannibals live there.")
                cannibal_eat = random.randint(1, 6)
                if cannibal_eat == 1:
                    get_eaten = "roasted over a bonfire"
                if cannibal_eat == 2:
                    get_eaten = "sauteed with lemon"
                if cannibal_eat == 3:
                    get_eaten = "pickled and saved for later"
                if cannibal_eat == 4:
                    get_eaten = "stuffed like a turkey and shared among the villiage folk."
                if cannibal_eat == 5:
                    get_eaten = "turned into soup"
                print("You get " + get_eaten)
                death_message()
                print("")
                print("Achievement Unlocked: 'Yummy Dinner'")
                print("")
                dinner_name = input("Please enter your name: " )
                dinner_dict = {
                    dinner_name:"Yummy Dinner"
                }
                with open("achievements.json", "w") as f:
                    json.dump(dinner_dict, f)
            else:
                print("")
                print("You continue on the path.")
                sleep(1)
                print("In the bushes, you hear something, and " + character_name + "'s brother Microwave pops out!")
                print("You win!")
                print("")
                print("Achievement Unlocked: 'Find Microwave'")
                print("")
                microwave_name = input("Please enter your name: " )
                microwave_dict = {
                    microwave_name:"Find Microwave"
                }
                with open("achievements.json", "w") as f:
                    json.dump(microwave_dict, f)
                print("")
                print("Thank you for playing! :)")
            



#adventure_game()
