from first_aid import first_aid_game
from adventure import adventure_game

def main():
    print("")
    print("Hello!")
    print("Choose your game:")
    print("- Adventure Game (input 'adventure')")
    print("- First Aid Test (input 'first aid')")
    print("- Something else I havent decided yet") #update this!!!
    print("")
    user_input = input()
    if user_input == "adventure": #has work to be done
        adventure_game()
    if user_input == "cpr": #has work to be done
        first_aid_game()

main()