# TO-DO:
# Add code fo CPR, Choking, and Burns
# Add a dictionary function which counts who completed the different sections completely

def first_aid_game():
    print("")
    print("Welcome to the First Aid Test! We will now see if you are qualified.")
    print("Do you want to try CPR, Choking, Decapitation, Burns, or 'Surprise Category'?")
    print("")
    input_aid_1 = input()
    if input_aid_1 == "cpr":
        print("CPR") #change
    if input_aid_1 == "choking":
        print("Choking") #change
    if input_aid_1 == "decapitation":
        print("")
        print("You can't save someone who's been decapitated, you silly goose.")
        print("")
    if input_aid_1 == "burns":
        print("Burns") #change
    if input_aid_1 == "surprise category":
        print("")
        print("You just used the helpful skills from the other category to save someone, congrats!")
        print("But upon a second glance, you now realize that it's your ex!")
        print("You look around and see a pair of scissors. What is the quickest way to kill them????")
        print("")
        print("Do you: slit the wrists (input 'a'), stab in stomach (input 'b'), or cut the jugular (neck) (input 'c')")
        input_surprise = input()
        if input_surprise == "c":
            print("")
            print("You have successfully killed your ex! They died in a fountain of their own blood.")
        else:
            print("")
            print("You failed to kill them in time. The ambulance arrived.")
            print("After your ex recovered, they skinned you alive with a potato peeler and then ran you over with their 18 wheeler.")
            print("")
                
first_aid_game()