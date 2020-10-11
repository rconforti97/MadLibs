# So we need a function that will take user input and input that into a array
# Welcome user
# What story would you like to do? Party, Solar System, Sports
# Once they choose a story prompt them to fill in the blanks
# Print the story calling the function.
import random

print("\nWelcome to the world of Rachel-Libs! Here are the topics to choose from:\n1) Autumn\n2) The Magic Computers"
      "\n3) Pumpkin Picking!\n\nPick your choice:"
      "(1-3)")
choice = input()

if choice is '1':
    print("\nYou have chosen, Autumn! I hope you enjoy :)")
    print("Write a name:")
    user_input_1 = input()
    print("Write a adjective. An adjective is a word you use to describe a person, place, or thing.")
    user_input_2 = input()
    print("Write a thing (plural)")
    user_input_3 = input()
    print("Write a thing (plural)")
    user_input_4 = input()
    print("Write a animal")
    user_input_5 = input()
    print("Write a verb ending in -ing")
    user_input_6 = input()
    print("Write a verb ending in -ing")
    user_input_7 = input()
    print("Write a adjective. An adjective is a word you use to describe a person, place, or thing.")
    user_input_8 = input()
    print("Write a number > 1")
    user_input_9 = input()
    print("Write a adjective. An adjective is a word you use to describe a person, place, or thing.")
    user_input_10 = input()
    print("Write a animal (plural)")
    user_input_11 = input()
    print("Write a name:")
    user_input_12 = input()
    print("Write a thing (plural)")
    user_input_13 = input()

    print(user_input_1 + " the squirrel had just climbed up the " + user_input_2 + " tree. It was the first day of "
          "autumn and time to gather as many " + user_input_3 + " and " + user_input_4 + " for winter feasting.\n"
          "Cheaster the " + user_input_5 + " asked his squirrel friend to take a break and join him for a little " +
          user_input_6 + " and " + user_input_7 + ". The two buddies had so much fun but the squirrel really needed"
          " to finish his gathering.\nHe returned to his " + user_input_8 + " home to find that " + user_input_9 + " "
          + user_input_10 + " " + user_input_11 + " where waiting for him to go to the fall festival party at "
          + user_input_12 + "'s house.\n" + user_input_1 + " realized that there wasn't going to be any more work"
          " that day. Today had been fun but tomorrow they'd need to collect more " + user_input_13 + " for the winter.")

if choice is '2':
    print("\nYou have chosen, The Magic Computer! Odd choice, I hope you enjoy.")
    print("Write a noun:")
    user_input_1 = input()
    print("Write a plural noun.")
    user_input_2 = input()
    print("Write a verb (present tense)")
    user_input_3 = input()
    print("Write a verb (present tense)")
    user_input_4 = input()
    print("Write a part of a body (plural)")
    user_input_5 = input()
    print("Write a adjective. An adjective is a word you use to describe a person, place, or thing.")
    user_input_6 = input()
    print("Write a plural noun")
    user_input_7 = input()
    print("Write a adjective. An adjective is a word you use to describe a person, place, or thing.")
    user_input_8 = input()

    print("Today, every student has a computer small enough to fit into their " + user_input_1 + ".\nStudents can solve"
          " any math problem by simply pushing the computer's little " + user_input_2 + ".\nComputers can add, "
          "multiply, divide, and " + user_input_3 + ".\nThey can also " + user_input_4 + " better then a human."
          "\nSome computers are " + user_input_5 + ". Others have a/an " + user_input_6 + " screen that shows all "
          "kinds of " + user_input_7 + " and " + user_input_8 + " figures.")


if choice is '3':
    print("\nYou have chosen, Pumpkin Picking! I hope you enjoy :)")
    print("Write a noun:")
    user_input_1 = input()
    print("Write a color.")
    user_input_2 = input()
    print("Write a color.")
    user_input_3 = input()
    print("Write a noun.")
    user_input_4 = input()
    print("Write a adjective. An adjective is a word you use to describe a person, place, or thing.")
    user_input_5 = input()
    print("Write a noun.")
    user_input_6 = input()
    print("Write a name of a vegetable.")
    user_input_7 = input()
    print("Write someones last name (plural).")
    user_input_8 = input()
    print("Write a verb.")
    user_input_9 = input()
    print("Write a adjective. An adjective is a word you use to describe a person, place, or thing.")
    user_input_10 = input()
    print("Write a name of a vegetable.")
    user_input_11 = input()
    print("Write a adjective. An adjective is a word you use to describe a person, place, or thing.")
    user_input_12 = input()
    print("Write a name of a vegetable.")
    user_input_13 = input()
    print("Write a noun:")
    user_input_14 = input()
    print("Write a exclamation:")
    user_input_15 = input()
    print("Write a adjective. An adjective is a word you use to describe a person, place, or thing.")
    user_input_16 = input()

    print("Fall has arrivied with a chill in the " + user_input_1 + ".\nThe leaves are turning " + user_input_2 +
          " and " + user_input_3 + ".\nNight time comes quicker, which usually means " + user_input_4 + "!\nBut today "
          "was a " + user_input_5 + " day. My " + user_input_6 + " went to the " + user_input_7 + " patch.\nThe "
          + user_input_8 + " took us on a hay " + user_input_9 + " to a big " + user_input_10 + " field.\nWe all got "
          "to pick a " + user_input_11 + " that was " + user_input_12 + "!\nYes, night comes quicker now that it's "
          "fall.\nBut tonight my " + user_input_13 + " sits by my " + user_input_14 + ", " + user_input_15 + ", what a "
          + user_input_16 + " day!")

else:
    print("Invalid input.")