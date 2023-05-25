def first_aid_game():
    print("")
    print("Welcome to the First Aid Test! We will now see if you are qualified.")
    print("Do you want to try CPR, Choking, Decapitation, Burns, or 'Surprise Category'?")
    print("")
    input_aid_1 = input()
    if input_aid_1 == "cpr":
        print("")
        print("Call 911 first")
        print("Then, do a cycle of 30 chest compressions and 2 breaths, and repeat.")
        print("Do chest compressions to the beat of 'staying alive', which is around 120 bpm, the necessary speed.")
    if input_aid_1 == "choking":
        print("")
        print("If someone is choking, do the Heimlich Maneuver.")
    if input_aid_1 == "decapitation":
        print("")
        print("You can't save someone who's been decapitated, you silly goose.")
        print("")
    if input_aid_1 == "burns":
        print("")
        print("If someone has bad burns, you need to rinse them under cool water and apply cold, wet compresses.")
        print("Do not apply any ointments yourself")
        print("If it's a really bad burn, or you get an infection, go to the hospital.")
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
            print("After your ex recovered, they skinned you alive with a potato peeler and then ran you over with their tractor.")
            print("")
                
#first_aid_game()