import random
import time
import sys
from colorama import Fore, Back, Style

def fancy_type_slow(*words):
    str = ''
    for item in words:
        str = str + item
    # str += "\n"
    for char in str:
        time.sleep(random.choice([
        0.06, 0.05, 0.03, 0.03,
        0.05, 0.03, 0.04, 0.05, 0.06, 0.04
        ]))
        sys.stdout.write(char)
        sys.stdout.flush()
        if (char == ".") or (char == "!"):
            time.sleep(0.7)
        if char == ",":
            time.sleep(0.4)

def fancy_type(*words):
    str = ''
    for item in words:
        str = str + item
    # str += "\n"
    for char in str:
        time.sleep(random.choice([
          0.03, 0.05, 0.04, 0.02,
          0.05, 0.03, 0.02, 0.05, 0.04, 0.01
        ]))
        sys.stdout.write(char)
        sys.stdout.flush()
        
def red_text(text):
    return (Fore.RED + text + Fore.WHITE)

def green_text(text):
    return (Fore.GREEN + text + Fore.WHITE)
            
def magenta_text(text):
    return (Fore.MAGENTA + text + Fore.WHITE)

def yellow_text(text):
    return (Fore.YELLOW + text + Fore.WHITE)

def cyan_text(text):
    return (Fore.CYAN + text + Fore.WHITE)
            
def bright_text(text):
    return (Style.BRIGHT + text + Style.NORMAL)

def first_setup():
    setup = 1
    while (setup != 0):
        fancy_type("Type 'y' or 'yes', not case sensitive, to say yes to a question: ")
        setup_question = input("")
        setup_question = setup_question.upper()
        if (setup_question == "YES") or (setup_question == "Y"):
            setup = 0
        else:
            fancy_type_slow("Try again.")
            print("\n")

    print("")

    setup = 1
    while (setup != 0):
        fancy_type("Type 'n' or 'no', not case sensitive, to say no to a question: ")
        setup_question = input("")
        setup_question = setup_question.upper()
        if (setup_question == "NO") or (setup_question == "N"):
            setup = 0
        else:
            fancy_type_slow("Try again.")
            print("\n")

    print("")

    setup = 1
    while (setup != 0):
        fancy_type("Type 'h' or 'hit', not case sensitive, to hit your hand: ")
        setup_question = input("")
        setup_question = setup_question.upper()
        if (setup_question == "HIT") or (setup_question == "H"):
            setup = 0
        else:
            fancy_type_slow("Try again.")
            print("\n")

    print("")

    setup = 1
    while (setup != 0):
        fancy_type("Type 's' or 'stand', not case sensitive, to stand with your hand's value: ")
        setup_question = input("")
        setup_question = setup_question.upper()
        if (setup_question == "STAND") or (setup_question == "S"):
            setup = 0
        else:
            fancy_type_slow("Try again.")
            print("\n")

    print("")

    question = 1
    while (question != 0):
        fancy_type_slow("So, are you ready to begin your Blackjack adventure? ")
        decisions_decisions = input("")
        decisions_decisions = decisions_decisions.upper()
        if (decisions_decisions == "YES") or (decisions_decisions == "Y"):
            question = 0
            print("")
            return 1
        elif (decisions_decisions == "NO") or (decisions_decisions == "N"):
            fancy_type_slow("I mean alright...I guess...If you say so...")
            return 0
        else:
            fancy_type_slow("I'll ask again...")
            print("\n")

def opening_lines():
    fancy_type_slow("“Ugh, not again,” you spout as the old wagon shutters, then dies. ")
    fancy_type_slow("Stranded on the road again, but this time, your money has gone dry. ")
    fancy_type_slow("All but your 50 dollar bill that Grandma gave you on her last Christmas. ")
    fancy_type_slow("You’ve been saving it for when you needed it most. ")
    fancy_type_slow("But surely, it won’t be enough.")
    print('\n')
    fancy_type_slow("The door creaks open, and you step out into the night sky, coughing up the smoke from your fried vehicle. ")
    fancy_type_slow("After pushing your car off the road and between the trees, there isn’t much else left for you to do, ")
    fancy_type_slow("so you begin to wander down the dark, lonely street.")
    print('\n')
    fancy_type_slow("But at the end of the road, where concrete turned to stone turned to dirt, you notice a light up ahead, on the top of a hill. ")
    print('\n')
    fancy_type_slow("As you waltz into the old, wooden shack, your eyes begin to light up with the fire of a thousand suns. ")
    fancy_type_slow("Roulette wheels! Poker tables! And in a dark corner of the abandoned casino, sits a dealer, shuffling cards for a new round of Blackjack. ")
    fancy_type_slow("That 50 dollars might just come in handy after all. Thanks, Grandma!")
    print('\n')
    fancy_type_slow("As you go to sit down at the table, you hear the dealer cough, then watch as he sits up")
    print("\n")
    fancy_type_slow("In a deep, and yet strained voice, the dealer, cloaked in darkness, poses a question to you")
    print("\n")

def end_day_1():
    fancy_type_slow("After playing a few rounds of Blackjack, the dealer points to the door. ")
    fancy_type_slow("Without questing his word, and with your winnings in hand, you scurry to the door, eager to get some rest after such a long day. ")
    fancy_type_slow("Making it back to your car, ditched on the side of the road, but no longer engulfed in smoke, you lay down, and close your eyes. It's time to rest.")