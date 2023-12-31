import random
import time
import sys
from colorama import Fore, Back, Style

def type_slow(*words):
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
        if (char == ":"):
            time.sleep(1)
        if char == ",":
            time.sleep(0.4)

def type(*words):
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
        
def red(text):
    return (Fore.RED + text + Fore.WHITE)

def green(text):
    return (Fore.GREEN + text + Fore.WHITE)
            
def magenta(text):
    return (Fore.MAGENTA + text + Fore.WHITE)

def yellow(text):
    return (Fore.YELLOW + text + Fore.WHITE)

def cyan(text):
    return (Fore.CYAN + text + Fore.WHITE)
            
def bright(text):
    return (Style.BRIGHT + text + Style.NORMAL)

def first_setup():
    setup = 1
    while (setup != 0):
        type("Type 'y' or 'yes', not case sensitive, to say yes to a question: ")
        setup_question = input("")
        setup_question = setup_question.upper()
        if (setup_question == "YES") or (setup_question == "Y"):
            setup = 0
        else:
            type_slow("Try again.")
            print("\n")

    print("")

    setup = 1
    while (setup != 0):
        type("Type 'n' or 'no', not case sensitive, to say no to a question: ")
        setup_question = input("")
        setup_question = setup_question.upper()
        if (setup_question == "NO") or (setup_question == "N"):
            setup = 0
        else:
            type_slow("Try again.")
            print("\n")

    print("")

    setup = 1
    while (setup != 0):
        type("Type 'h' or 'hit', not case sensitive, to hit your hand: ")
        setup_question = input("")
        setup_question = setup_question.upper()
        if (setup_question == "HIT") or (setup_question == "H"):
            setup = 0
        else:
            type_slow("Try again.")
            print("\n")

    print("")

    setup = 1
    while (setup != 0):
        type("Type 's' or 'stand', not case sensitive, to stand with your hand's value: ")
        setup_question = input("")
        setup_question = setup_question.upper()
        if (setup_question == "STAND") or (setup_question == "S"):
            setup = 0
        else:
            type_slow("Try again.")
            print("\n")

    print("")

    question = 1
    while (question != 0):
        type_slow("So, are you ready to begin your Blackjack adventure? ")
        decisions_decisions = input("")
        decisions_decisions = decisions_decisions.upper()
        if (decisions_decisions == "YES") or (decisions_decisions == "Y"):
            question = 0
            print("")
            return True
        elif (decisions_decisions == "NO") or (decisions_decisions == "N"):
            type_slow("I mean alright...I guess...If you say so...")
            sys.exit()
        else:
            type_slow("I'll ask again...")
            print("\n")

def opening_lines():
    type_slow("“Ugh, not again,” you spout as the old wagon shutters, then dies. ")
    type_slow("Stranded on the road again, but this time, your money has gone dry. ")
    type_slow("All but your 50 dollar bill that Grandma gave you on her last Christmas. ")
    type_slow("You've been saving it for when you needed it most. ")
    type_slow("But surely, it won't be enough.")
    print('\n')
    type_slow("The door creaks open, and you step out into the night sky, coughing up the smoke from your fried vehicle. ")
    type_slow("After pushing your car off the road and between the trees, there isn't much else left for you to do, ")
    type_slow("so you begin to wander down the dark, lonely street.")
    print('\n')
    type_slow("But at the end of the road, where concrete turned to stone turned to dirt, you notice a light up ahead, on the top of a hill. ")
    print('\n')
    type_slow("As you waltz into the old, wooden shack, your eyes begin to light up with the fire of a thousand suns. ")
    type_slow("Roulette wheels! Poker tables! And in a dark corner of the abandoned casino, sits a dealer, shuffling cards for a new round of Blackjack. ")
    type_slow("That 50 dollars might just come in handy after all. Thanks, Grandma!")
    print('\n')
    type_slow("As you go to sit down at the table, you hear the dealer cough, then watch as he sits up.")
    print("\n")
    type_slow("In a deep, and yet strained voice, the dealer, cloaked in darkness, poses a question to you.")
    print("\n")

def dealer_tale():
    type_slow(red("What is it you want from me? "))
    type_slow(red("Can't you see YOU'RE WASTING MY TIME?"))
    print("\n")
    type_slow("The dealer sits up from his shadow and into the light from the flickering lamp above. ")
    type_slow("You get a close look at a dark green, glass eye, glowing by a scar across his cheek. ")
    type_slow("Around his waste sits a shining grey revolver, in each chamber a bullet ready to be fired.")
    print("\n")
    type_slow(red("Don't play funny with me, you rat. "))
    type_slow(red("I've put down much stronger. "))
    type_slow(red("I'll end your progress right here, right now. "))
    type_slow(red("Just say yes, and it'll all be over. "))
    decisions_decisions = input("")
    decisions_decisions = decisions_decisions.upper()
    if (decisions_decisions == "YES"):
        type("The Dealer pulls the revolver from his waste and shoots you. ")
        type("As you fall to the ground, and fade from this world, you see the dealer walk up to your body. ")
        type("He aims the gun down, and shoots again. And again. And once more.")
        
    elif (decisions_decisions == "NO") or (decisions_decisions == "N"):
        type_slow("That's what I THOUGHT. ")
        type_slow("I hope to never have this conversation again. ")
        print("\n")
        return 0
    else:
        type_slow(red("Don't think you're my only visiter. "))
        type_slow(red("And certainly don't think you can just walk all over me. "))
        type_slow(red("This is MY game. You're sitting at MY table. You follow MY rules. "))
        type_slow(red("Lets not talk about this again."))
        print("\n")

def end_day_1():
    type_slow("After playing a few rounds of Blackjack, the dealer points to the door. ")
    type_slow("Without questing his word, and with your winnings in hand, you scurry to the door, eager to get some rest after such a long day. ")
    type_slow("Making it back to your car, ditched on the side of the road, but no longer engulfed in smoke, you lay down, and close your eyes. It's time to rest.")

def end_day_2():
    type_slow("After playing a few rounds of Blackjack, the dealer points to the door. ")
    type_slow("Without questing his word, and with your winnings in hand, you scurry to the door, eager to get some rest. ")
    type_slow("Making it back to your car, ditched on the side of the road, you lay down, and close your eyes. It's time to rest.")

def make_random_event_list(time, rank):
    if (time == 0) and (rank == 0):
        count = 3
    if (time == 0) and (rank == 1):
        count = 0
    if (time == 0) and (rank == 2):
        count = 0
    if (time == 0) and (rank == 3):
        count = 0
    if (time == 0) and (rank == 4):
        count = 0
    if (time == 0) and (rank == 5):
        count = 0
    if (time == 1) and (rank == 0):
        count = 0
    if (time == 1) and (rank == 1):
        count = 0
    if (time == 1) and (rank == 2):
        count = 0
    if (time == 1) and (rank == 3):
        count = 0
    if (time == 1) and (rank == 4):
        count = 0
    if (time == 1) and (rank == 5):
        count = 0
    if (time == -1) and (rank == -1):
        count = 29
    event_list = list(range(count))
    random.shuffle(event_list)
    return event_list


# Day Summary


def day_summary(balance, previous_balance, rank, day_count, quote_list):
    cheer = list(range(6))
    random.shuffle(cheer)
    index = cheer[0]
    if index == 0:
        type_slow("Congrats! ")
    if index == 1:
        type_slow("Hurray! ")
    if index == 2:
        type_slow("Yippee! ")
    if index == 3:
        type_slow("Woo-hoo! ")
    if index == 4:
        type_slow("Yessir! ")
    if index == 5:
        type_slow("Yesss! ")

    if day_count == 1:
        type_slow("You've survived " + yellow(bright(str(day_count) + " day")) + "!")
    else:
        type_slow("You've survived " + yellow(bright(str(day_count) + " days")) + "!")

    print("\n")

    if day_count == 1:
        type_slow("You started your journey with just " + green(bright("$" + str(previous_balance))) + ". ")
    else:
        type_slow("Yesterday, at this time, you had " + green(bright("$" + str(previous_balance))) + ". ")

    print("")

    if (balance - previous_balance) > 0:
        type_slow("Since then, you've accumulated " + green(bright("$" + str(balance - previous_balance))) + ". ")
    elif (balance - previous_balance) < 0:
        type_slow("Since then, you've managed to lose " + red(bright("$" + str(previous_balance - balance))) + ". ")
    else:
        type_slow("Somehow, your net earnings today was 0. Goose egg. No money. Disappointing. ")

    print("")

    type_slow("That brings you to a grand total of " + green(bright("$" + str(balance))) + "! ")

    if rank == 0:
        type_slow("Let's not get too far ahead of ourselves though, you're still quite poor.")
    elif rank == 1:
        type_slow("You definately have some money. The keyword is 'some'.")
    elif rank == 2:
        type_slow("You've amassed signifigant earnings. Nicely done.")
    elif rank == 3:
        type_slow("You must have some heavy pockets, huh.")
    elif rank == 4:
        type_slow("Where do you even keep all that?")
    elif rank == 5:
        type_slow("So close to being a millionaire! Can you do it?")

    print("\n")

    congrats = list(range(8))
    random.shuffle(congrats)
    index = congrats[0]
    if index == 0:
        type_slow("Good progress so far, pal. Keep it up.")
    elif index == 1:
        type_slow("For what it's worth, I think you're doing alright.")
    elif index == 2:
        type_slow("I mean, you could definately make more money, but hey it's a good start.")
    elif index == 3:
        type_slow("Congrats on all the hard work so far. It's nice to know you're still alive.")
    elif index == 4:
        type_slow("I would probably wipe that smile off that face if I were you. Just kidding, you're awesome.")
    elif index == 5:
        type_slow("Do you think maybe you could be a bit better at Blackjack? Just think about it.")
    elif index == 6:
        type_slow("I like your work ethic. Your grandma would be proud.")
    elif index == 7:
        type_slow("If there's one thing I've learned, it's that you must never back down, and never give up.")

    print("")

    quote_setup = list(range(7))
    random.shuffle(quote_setup)
    index = quote_setup[0]
    if index == 0:
        type_slow("I'll leave you with a quote: ")
    if index == 1:
        type_slow("Here's a little bit of inspiration for you: ")
    if index == 2:
        type_slow("Here's a quote my dad used to say: ")
    if index == 3:
        type_slow("This quote always gets me going: ")
    if index == 4:
        type_slow("If you ever feel lost, just remember: ")
    if index == 5:
        type_slow("Don't forget what the bible taught you: ")
    if index == 6:
        type_slow("You know what you need right now? A quote, from the heart: ")

    index = quote_list.pop()
    if index == 0:
        type_slow("\"Stars aren't far away. They're just really small. They're so small that all 17 of them could fit into the earth. That's why we can't get to them. They move away so the planet doesn't eat them and only show up at night when the earth is sleeping.\"")
    if index == 1:
        type_slow("\"You may have breathed the same air a dinosaur breathed 1000s of years ago. If you don't think that's the tightest shit then get out of my face.\"")
    if index == 2:
        type_slow("\"Don't be afraid to fail. Be afraid to get emotionally invested and then fail.\"")
    if index == 3:
        type_slow("\"Every corpse on Everest was once an extremely motivated person.\"")
    if index == 4:
        type_slow("\"I honest to God thought Santa Claus was real for the longest time. Mom and Dad just never told me. My parents are fucking cruel.\"")
    if index == 5:
        type_slow("\"Every tattoo is a temporary tattoo, because we are all slowly dying.\"")
    if index == 6:
        type_slow("\"The reason you have to follow your dreams is because even your dreams are trying to get away from you.\"")
    if index == 7:
        type_slow("\"If you give up on your dreams, that may free up some time to get some actual stuff done\"")
    if index == 8:
        type_slow("\"If you hate yourself, remember that you are not alone. A lot of other people hate you too.\"")
    if index == 9:
        type_slow("\"The trash gets picked up tomorrow. Be ready.\"")
    if index == 10:
        type_slow("\"I'm not your fucking therapst, stop using me for emotional advice.\"")
    if index == 11:
        type_slow("\"No matter how many motivational quotes you know, you will remain a pathetic loser. Yesterday, today, and tomorrow. No matter how much you make, what degree you earn or what lie you tell yourself. A big flop at life you will remain. Don't doubt it for a minute. That's not even addressing your disgustinly deformed physique.\"")
    if index == 12:
        type_slow("\"Good Moms have sticky floors, messy kitchens, laundry piles, dirty ovens, and happy kids.\"")
    if index == 13:
        type_slow("\"Before you can love someone else you have to learn to love yourself so there's no chance of that happening.\"")
    if index == 14:
        type_slow("\"There was a safety meeting at work today. They asked me, 'What steps would you take in the event of a fire?' 'Fucking big ones' was the wrong answer.\"")
    if index == 15:
        type_slow("\"I walk around like everything's fine, but deep down, inside my shoe, my sock is sliding off.\"")
    if index == 16:
        type_slow("\"Life would be a lot easier if it wasn't so hard.\"")
    if index == 17:
        type_slow("\"I can't brain today. I have the dumb.\"")
    if index == 18:
        type_slow("\"If you don't want to be mistaken for a doormat, get off the damn floor.\"")
    if index == 19:
        type_slow("\"You know it's cold outside when you go outside and it's cold.\"")
    if index == 20:
        type_slow("\"If I had to rate you from 1 to 10, I'd give you a 9, because I'm the 1 you're missing.\"")
    if index == 21:
        type_slow("\"Have you ever wondered why you can't taste your tongue?\"")
    if index == 22:
        type_slow("\"Freedom means the right to yell, \"THEATRE!\" in a crowded fire.\"")
    if index == 23:
        type_slow("\"Whatever you're doing, always give 100 percent. Unless you're donating blood.\"")
    if index == 24:
        type_slow("\"Would you believe that my neighbor came ringing my doorbell at 2:00 this morning? Luckily for him, I was still up playing bagpipes.\"")
    if index == 25:
        type_slow("\"If a man said he'll fix it, he'll fix it. There is no need to nag him every 6 months about it.\"")
    if index == 26:
        type_slow("\"Every form has its own meaning. Every man creates his meaning and form and goal. Why is it so important - what others have done? Why does it become sacred by the mere fact of not being your own? Why is anyone and everyone right - so long as it's not yourself? Why does the number of those others take the place of truth? Why is truth made a mere matter of arithmetic - and only of addition at that? Why is everything twisted out of all sense to fit everything else? There must be some reason. I don't know. I've never known it. I'd like to understand.\"")
    if index == 27:
        type_slow("\"Grief, I've learned, is really just love. It's all the love you want to give, but cannot. All that unspent love gathers up in the corners of your eyes, the lump in your throat, and in that hollow part of your chest. Grief is just love with no place to go.\"")
    if index == 28:
        type_slow("\"Bananas! Bananas! Bananas! Bananas! Bananas! Bananas! Bananas! Bananas!\"")


# Daytime Events


def random_day_event_poor(event, balance, is_alive, status_effects, items):
    """
    0 dollars to 1,000 dollars
    """
    if event == 0:
        type_slow("As the sun shines through the car window, you notice a bright green bill tucked between the seat cushions. Must be your lucky day. ")
        print("\n")
        x = random.randint(0, 4)
        list = [5, 10, 20, 50, 100]
        type_slow("That's another " + green(bright("$" + str(list[x]))) + " dollars")
        return (balance + list[x]), is_alive
    if event == 1:
        type_slow("As you sit up from your slumber, you hear a vehicle approaching. As it draws near, you can see an old lady inside. ")
        type_slow("You open the door of your broken down car, and attempt to wave her down. ")
        type_slow("The old lady's vehicle slows down, but as you get a closer look at her disgruntled face, you notice her lift her middle finger in your direction. ")
        type_slow("She speeds off into the distance. What a bitch.")
        return balance, is_alive
    if event == 2:
        type_slow("For some reason, you woke up with a strong motivation in your eye. ")
        type_slow("Today must be the day. ")
        type_slow("To capitalize on this productivity, you hop out of the backseat, and pop open the hood of your fried car. ")
        type_slow("As you poke your head in, trying to figure out the issue, you hear a hiss, and then notice a green wire, that appears to be rattling. ")
        status_effects.append("Poisoned")
        return balance, is_alive

def random_day_event_cheap(event):
    """
    1,000 dollars to 10,000 dollars
    """

def random_day_event_modest(event):
    """
    10,000 to 100,000
    """

def random_day_event_rich(event):
    """
    100,000 to 500,000
    """

def random_day_event_doughman():
    """
    500,000 to 900,000
    """

def random_day_event_nearly_there():
    """
    900,000 to 1,000,000
    """


# Nighttime Events


def random_night_event_poor():
    """
    0 dollars to 1,000 dollars
    """

def random_night_event_cheap():
    """
    1,000 dollars to 10,000 dollars
    """

def random_night_event_modest():
    """
    10,000 to 100,000
    """

def random_night_event_rich():
    """
    100,000 to 500,000
    """

def random_night_event_doughman():
    """
    500,000 to 900,000
    """

def random_night_event_nearly_there():
    """
    900,000 to 1,000,000
    """

def use_later():
    "You know why I like blackjack? Because it's a losing game, disguised as a fair chance."
    "That is, unless you try and count cards"
    "Can't do that here though, these boys are shuffled real good, heheh"

def drunk_shuffle_cards():
    deck_range=range(1,85)
    deck=list(deck_range)
    random.shuffle(deck)
    return deck

def drunk_check_suit(card):
    if card <= 10:
        return "of Hippos"
    elif card <= 18:
        return "of Large Green Monsters"
    elif card <= 35:
        return "of Squares"
    elif card <= 50:
        return "of Candycanes"
    elif card <= 63:
        return "of Starfishes"
    elif card <= 75:
        return "of Jupiters"
    elif card <= 80:
        return "of Unicorns"
    elif card <= 84:
        return "of Suns"
    
def drunk_card_int(card):
    card_int = card%21
    if card_int == 0:
        card_int = 21
    return(card_int)
    
def drunk_check_value(card):
    card_value=card%21
    if card_value == 1:
        return "One"
    elif card_value == 2:
        return "Two"
    elif card_value == 3:
        return "Three"
    elif card_value == 4:
        return "4"
    elif card_value == 5:
        return "Five"
    elif card_value == 6:
        return "Six"
    elif card_value == 7:
        return "7"
    elif card_value == 8:
        return "Eight"
    elif card_value == 9:
        return "Nine"
    elif card_value == 10:
        return "Ten"
    elif card_value == 11:
        return "Jack"
    elif card_value == 12:
        return "Queen"
    elif card_value == 13:
        return "King"
    elif card_value == 14:
        return "Rook"
    elif card_value == 15:
        return "Spade"
    elif card_value == 16:
        return "Dragon"
    elif card_value == 17:
        return "Jester"
    elif card_value == 18:
        return "Balloon"
    elif card_value == 19:
        return "Baboon"
    elif card_value == 20:
        return "Tiger"
    elif card_value == 0:
        return "Blackjack"

def drunk_print_hand_value(hand_value):
    type("Your cards have a value of ", green(bright(str(hand_value))))
    print("")

def drunk_print_dealer_hand_value(dealer_hand_value):
    type(red("The dealer's cards have a value of " + bright(str((dealer_hand_value)))))
    print("\n")

def drunk_check_value_21_or_over(value, goal):
    if value == goal:
        return "Blackjack"
    elif value > goal:
        return "Bust"
    else:
        return

def drunk_blackjack(bet, balance):
    game_running = 1
    while game_running == 1:
        goal = random.randint(85, 120)
        type("You're trying to get to " + green(bright(str(goal))))
        print("\n")
        deck_of_cards = drunk_shuffle_cards()
        card_one = deck_of_cards.pop(0)
        card_one_value = drunk_check_value(card_one)
        card_one_suit = drunk_check_suit(card_one)

        if ((card_one_value[0] == "A") or (card_one_value[0] == "E")):
            type("Your first card is an ", magenta(bright(card_one_value + " " + card_one_suit)))
        else:
            type("Your first card is a ", magenta(bright(card_one_value + " " + card_one_suit)))

        print("")

        dealer_card_one = deck_of_cards.pop(0)
        dealer_card_one_value = drunk_check_value(dealer_card_one)
        dealer_card_one_suit = drunk_check_suit(dealer_card_one)

        if (dealer_card_one_value == "Eight"):
            type(red("The dealer's first card is an " + bright(dealer_card_one_value + " " + dealer_card_one_suit)))
        else:
            type(red("The dealer's first card is a " + bright(dealer_card_one_value + " " + dealer_card_one_suit)))
        
        print("\n")

        card_two = deck_of_cards.pop(0)
        card_two_value = drunk_check_value(card_two)
        card_two_suit = drunk_check_suit(card_two)
        if ((card_two_value == "Ace") or (card_two_value == "Eight")):
            type("Your second card is an " + magenta(bright(card_two_value + " " + card_two_suit)))
        else:
            type("Your second card is a " + magenta(bright(card_two_value + " " + card_two_suit)))
            
        print("")

        dealer_card_two = deck_of_cards.pop(0)
        dealer_card_two_value = drunk_check_value(dealer_card_two)
        dealer_card_two_suit = drunk_check_suit(dealer_card_two)
        
        dealer_card_one_int = drunk_card_int(dealer_card_one)
        dealer_card_two_int = drunk_card_int(dealer_card_two)
        dealer_current_hand_int = dealer_card_one_int + dealer_card_two_int

        type(red("The dealer's second card is face down"))
            
        print("\n")
        type(red("As of now, the dealer's cards have a known value of " + bright(str(dealer_card_one_int))))

        print("")

        card_one_int = drunk_card_int(card_one)
        card_two_int = drunk_card_int(card_two)
        current_hand_int = card_one_int + card_two_int

        drunk_print_hand_value(current_hand_int)

        # Gameplay loop (Hitting repeatedly, then dealer hitting repeatedly)
        dealer_story = 0
        response = 0
        while response == 0:
            type("Would you like to hit or stand? ")
            
            decisions_decisions = input ('')
            print("") # Prints a line for spacing purposes
            decisions_decisions = decisions_decisions.upper()

            if (decisions_decisions == "HIT") or (decisions_decisions == "H"):
                additional_card = deck_of_cards.pop(0)
                additional_card_value = drunk_check_value(additional_card)
                additional_card_suit = drunk_check_suit(additional_card)
                if (additional_card_value == "Eight"):
                  type("Your next card is an " + magenta(bright( additional_card_value + " " + additional_card_suit)))
                else:
                  type("Your next card is a " + magenta(bright( additional_card_value + " " + additional_card_suit)))
                  
                print("")

                additional_card_int = drunk_card_int(additional_card)
                current_hand_int = current_hand_int + additional_card_int

                drunk_print_hand_value(current_hand_int)

                game_over = drunk_check_value_21_or_over(current_hand_int, goal)

                if game_over == "Bust":
                    loss = int(bet * (random.randint(0, 40)/12))
                    print("")
                    type(red(bright("You went over " + str(goal) + "! Bust! You Lose!")))
                    print("")
                    type(red(bright("You bet " + green("$" + str(bet)) + ", and ultimately lost " + green("$") + str(loss))))
                    print("\n")
                    type(red(bright("Your new balance is " + green("$" + str(balance) + red(" - $" + str(loss)) + green(" = $" + str((balance - loss)))))))
                    print("")
                    return balance-loss
                elif game_over == "Blackjack":
                    print("")
                    type(yellow(bright("You reached the goal! Yippee! Hallelujah!")))
                    print("")
                    type(yellow(bright("With an innital bet of " + green("$" + str(bet)) + yellow(", you've tripled it!"))))
                    print("\n")
                    type(yellow(bright("Your new balance is " + green("$" + str(balance) + " + $" + str(bet*2) + " = $" + str(balance+(2*bet))))))
                    print("")
                    return balance + (2*bet)

            elif (decisions_decisions == "STAND") or (decisions_decisions == "S"):

                type("You decided to stand at a value of ", green(bright(str(current_hand_int))))
                print("\n")

                if ((dealer_card_two_value == "Eight")):
                    type(red("The dealer's second card is an " + bright(dealer_card_two_value + " " + dealer_card_two_suit)))
                else:
                    type(red("The dealer's second card is a " + bright(dealer_card_two_value + " " + dealer_card_two_suit)))

                print("")

                drunk_print_dealer_hand_value(dealer_current_hand_int)

                dealer_playing = 0
                while dealer_playing == 0:
                    if (goal == dealer_current_hand_int > current_hand_int):
                        type(red("The dealer stands at " + bright(str(dealer_current_hand_int))))
                        print("\n")
                        type(red(bright("The dealer gets a Blackjack and wins! Too bad! So sad! Get good, kiddo!")))
                        print("")
                        type(red(bright("You lost your bet of " + green("$" + str(bet)))))
                        print("\n")
                        type(red(bright("Your new balance is " + green("$" + str(balance) + red(" - $" + str(bet)) + green(" = $" + str((balance - bet)))))))
                        print("")
                        return balance - bet
                    elif (goal > dealer_current_hand_int > current_hand_int):
                        type(red("The dealer stands at " + bright(str(dealer_current_hand_int))))
                        print("\n")
                        type(red(bright("The dealer wins! Too bad! So sad! Stay mad!")))
                        print("")
                        type(red(bright("You lost your bet of " + green("$" + str(bet)))))
                        print("\n")
                        type(red(bright("Your new balance is " + green("$" + str(balance) + red(" - $" + str(bet)) + green(" = $" + str((balance - bet)))))))
                        print("")
                        return balance - bet
                    elif (dealer_current_hand_int > goal):
                        type(magenta(bright("The dealer went over 21! Bust! You Win!")))
                        print("")
                        type(magenta(bright("With an innital bet of " + green("$" + str(bet)) + magenta(", you've doubled it!"))))
                        print("\n")
                        type(magenta(bright("Your new balance is " + green("$" + str(balance) + " + $" + str(bet) + " = $" + str(balance + bet)))))
                        print("")
                        return (balance - bet) + (bet*2)
                    elif (dealer_current_hand_int == current_hand_int):
                        type(red("The dealer stands at " + bright(str(dealer_current_hand_int))))
                        print("\n")
                        type(cyan(bright("Since you and the dealer have the same value, it's a draw. So, so very lame.")))
                        print("")
                        type(cyan(bright("You win back your bet of " + green("$" + str(bet)))))
                        print("\n")
                        type(cyan(bright("Your balance has returned to " + green("$" + str(balance)))))
                        print("")
                        return balance
                    elif ((dealer_current_hand_int >= int(goal * 0.81))):
                        type(red("The dealer stands at " + str(dealer_current_hand_int)))
                        print("\n")
                        type(magenta(bright("Congrats! You Win! Get REKT, dealer!")))
                        print("")
                        type(magenta(bright("With an innital bet of " + green("$" + str(bet)) + magenta(", you've doubled it!"))))
                        print("\n")
                        type(magenta(bright("Your new balance is " + green("$" + str(balance) + " + $" + str(bet) + " = $" + str(balance + bet)))))
                        print("")
                        return (balance + bet)
                    else:
                        type(red("The dealer's cards are a value under " + str(int(goal * 0.81)) + " so they hit"))

                        print("")

                        additional_dealer_card = deck_of_cards.pop(0)
                        additional_dealer_card_value = drunk_check_value(additional_dealer_card)
                        additional_dealer_card_suit = drunk_check_suit(additional_dealer_card)
                        if (additional_dealer_card_value == "Eight"):
                            type(red("The dealer's next card is an " + bright(additional_dealer_card_value + " " + additional_dealer_card_suit)))
                        else:
                            type(red("The dealer's next card is a " + bright(additional_dealer_card_value + " " + additional_dealer_card_suit)))

                        print("")

                        additional_dealer_card_int = drunk_card_int(additional_dealer_card)
                        dealer_current_hand_int = dealer_current_hand_int + additional_dealer_card_int
                        drunk_print_dealer_hand_value(dealer_current_hand_int)

            else:
                if dealer_story == 0:
                    type(red("I didn't quite catch that."))
                    print("\n")
                    dealer_story += 1
                elif dealer_story == 1:
                    type(red("Do ya mind speaking up?"))
                    print("\n")
                    dealer_story += 1
                elif dealer_story == 2:
                    type(red("Speak louder."))
                    print("\n")
                    dealer_story += 1
                elif dealer_story == 3:
                    type(red("Can't ya hear me?"))
                    print("\n")
                    dealer_story += 1
                elif dealer_story == 4:
                    type(red("You gotta hit it or stand, kid."))
                    print("\n")
                    dealer_story += 1
                elif dealer_story == 5:
                    type(red("Pick an option. Now."))
                    print("\n")

    type("")

