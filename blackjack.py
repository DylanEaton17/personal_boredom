import random
from colorama import Fore, Back, Style
import time
import random
import sys
import story

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
        if char == ",":
            time.sleep(0.4)

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

def shuffle_cards():
    deck_range=range(1,53)
    deck=list(deck_range)
    random.shuffle(deck)
    return deck

def check_suit(card):
    if card <= 13:
        return "of Hearts"
    elif card <= 26:
        return "of Clubs"
    elif card <= 39:
        return "of Diamonds"
    elif card <= 52:
        return "of Spades"
    
def card_int(card, ace):
    card_int = card%13
    if card_int > 10:
            card_int = 10
    elif card_int == 0:
            card_int = 10
    elif card_int == 1:
            ace = ace + 1
    return(card_int, ace)
    
def check_value(card):
    card_value=card%13
    if card_value == 1:
        return "Ace"
    elif card_value == 2:
        return "Two"
    elif card_value == 3:
        return "Three"
    elif card_value == 4:
        return "Four"
    elif card_value == 5:
        return "Five"
    elif card_value == 6:
        return "Six"
    elif card_value == 7:
        return "Seven"
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
    elif card_value == 0:
        return "King"

def print_hand_value(hand_value, ace):
    if (ace > 0) & ((hand_value + 10) < 21):
        type("Your cards have a value of ", green(bright(str(hand_value))) + ", or " + green(bright(str((hand_value + 10)))) + " since you have an ace")
        print("")
    elif (ace > 0) & ((hand_value + 10) == 21):
        type("Your cards have a value of ", green(bright(str(hand_value + 10))))
    else:
        type("Your cards have a value of ", green(bright(str(hand_value))))
        print("")

def print_dealer_hand_value(dealer_hand_value, dealer_ace):
    if (dealer_ace > 0) & ((dealer_hand_value + 10) < 21):
        type(red("The dealer's cards have a value of " + bright(str((dealer_hand_value))) + ", or " + bright( str((dealer_hand_value + 10))) + " since they have an ace"))
        print("\n")
    elif (dealer_ace > 0) & ((dealer_hand_value + 10) == 21):
        type(red("The dealer's cards have a value of " + bright(str((dealer_hand_value + 10)))))
    else:
        type(red("The dealer's cards have a value of " + bright(str((dealer_hand_value)))))
        print("\n")

def check_value_21_or_over(value, ace):
    if value == 21:
        return "Blackjack"
    elif (ace>0) & (value+10==21):
        return "Blackjack"
    elif value > 21:
        return "Bust"
    else:
        return
    
def choose_bet(balance, min_bet=1):
    print("")
    currently_betting = 1
    angry_dealer=0
    while currently_betting != 0:
        bet = None
        while bet is None:
            type("The dealer expects you to bet at least " + green(bright("$" + str(min_bet))))
            print("")
            type("How much would you like to bet? ")
            try:
                bet = int(input(""))
            except ValueError:
                print("")
                type(red("The dealer looks at you confused. Perhaps he didn't hear you."))
                print("\n")

        print("")
        if(int(bet)<=balance) and (int(bet)>0):
            return int(bet)
        elif((int(bet) < min_bet) and (angry_dealer==0)):
            type_slow(red("The dealer looks at you with an aggressive eye. Maybe try betting more cash!"))
            print("\n")
            angry_dealer += 1
        elif((int(bet) < min_bet) and (angry_dealer==1)):
            type_slow(red("The dealer is infuriated. You've insulted him. You should bet more cash."))
            print("\n")
            angry_dealer += 1
        elif((int(bet) < min_bet) and (angry_dealer==2)):
            type_slow(red("The dealer gets up from his chair and charges his relover. Bet more cash. You'll regret it if you don't."))
            print("\n")
            angry_dealer += 1
        elif((int(bet) < min_bet) and (angry_dealer==3)):
            type_slow(red("The dealer fires three shots into your chest. You bleed out, and as you fade from reality, you see the dealer reach into your pockets, and take every last penny from your lifeless body."))
            print("")
            return "dead"
        else:
            type(red("The dealer looks at you confused. Perhaps he didn't hear you."))
            print("\n")

def blackjack_main(bet, balance):
    game_running = 1
    while game_running == 1:
        deck_of_cards = shuffle_cards()
        card_one = deck_of_cards.pop(0)
        card_one_value = check_value(card_one)
        card_one_suit = check_suit(card_one)

        if ((card_one_value == "Ace") or (card_one_value == "Eight")):
            type("Your first card is an ", magenta(bright(card_one_value + " " + card_one_suit)))
        else:
            type("Your first card is a ", magenta(bright(card_one_value + " " + card_one_suit)))

        print("")

        dealer_card_one = deck_of_cards.pop(0)
        dealer_card_one_value = check_value(dealer_card_one)
        dealer_card_one_suit = check_suit(dealer_card_one)

        if ((dealer_card_one_value == "Ace") or (dealer_card_one_value == "Eight")):
            type(red("The dealer's first card is an " + bright(dealer_card_one_value + " " + dealer_card_one_suit)))
        else:
            type(red("The dealer's first card is a " + bright(dealer_card_one_value + " " + dealer_card_one_suit)))
        
        print("\n")

        card_two = deck_of_cards.pop(0)
        card_two_value = check_value(card_two)
        card_two_suit = check_suit(card_two)
        if ((card_two_value == "Ace") or (card_two_value == "Eight")):
            type("Your second card is an " + magenta(bright(card_two_value + " " + card_two_suit)))
        else:
            type("Your second card is a " + magenta(bright(card_two_value + " " + card_two_suit)))
            
        print("")

        dealer_card_two = deck_of_cards.pop(0)
        dealer_card_two_value = check_value(dealer_card_two)
        dealer_card_two_suit = check_suit(dealer_card_two)
        
        dealer_ace = 0
        dealer_card_one_int, dealer_ace = card_int(dealer_card_one, dealer_ace)
        dealer_card_two_int, dealer_ace = card_int(dealer_card_two, dealer_ace)
        dealer_current_hand_int = dealer_card_one_int + dealer_card_two_int

        game_over_dealer = check_value_21_or_over(dealer_current_hand_int, dealer_ace)
        if game_over_dealer == "Blackjack":
            if ((dealer_card_two_value == "Ace")):
                type(red("The dealer's second card is an " + bright(dealer_card_two_value + " " + dealer_card_two_suit)))
                print("")
                type(red("The dealer's cards have a value of 21 ;)"))
            else:
                type(red("The dealer's second card is a " + bright(dealer_card_two_value + " " + dealer_card_two_suit)))
                print("")
                type(red("The dealer's cards have a value of 21 ;)"))
        else:
            type(red("The dealer's second card is face down"))
            
        print("")
        
        # prints dealer's starting value
        if game_over_dealer != "Blackjack":
            if dealer_card_one_int == 1:
                print("")
                type(red("As of now, the dealer's cards have a known value of " + bright("1") + " or " + bright("11") + ", since they have an ace"))
            else:    
                print("")
                type(red("As of now, the dealer's cards have a known value of " + bright(str(dealer_card_one_int))))

        print("")

        ace = 0
        card_one_int, ace = card_int(card_one, ace)
        card_two_int, ace = card_int(card_two, ace)
        current_hand_int = card_one_int + card_two_int

        print_hand_value(current_hand_int, ace)

        game_over = check_value_21_or_over(current_hand_int, ace)

        if game_over == "Bust":
            print("\n")
            type(red(bright("You went over 21! Bust! You Lose!")))
            print("")
            type(red(bright("You lost your bet of " + green("$" + str(bet)))))
            print("\n")
            type(red(bright("Your new balance is " + green("$" + str(balance) + red(" - $" + str(bet)) + green(" = $" + str((balance - bet)))))))
            print("")
            return balance - bet
        elif (game_over == "Blackjack") & (game_over_dealer == "Blackjack"):
            print("\n")
            type(cyan(bright("You and the dealer both got a Blackjack. How boring.")))
            print("")
            type(cyan(bright("You win back your bet of " + green("$" + str(bet)))))
            print("\n")
            type(cyan(bright("Your balance has returned to " + green("$" + str(balance)))))
            print("")
            return balance
        elif game_over == "Blackjack":
            print("\n")
            type(yellow(bright("You got a Blackjack! You Win! Huzzah! Bon Voyage!")))
            print("")
            type(yellow(bright("With an innital bet of " + green("$" + str(bet)) + yellow(", you've tripled it!"))))
            print("\n")
            type(yellow(bright("Your new balance is " + green("$" + str(balance) + " + $" + str(bet*2) + " = $" + str((balance)+(2*bet))))))
            print("")
            return (balance)+(bet*2)
        elif game_over_dealer == "Blackjack":
            print("")
            type(red(bright("Damn the dealer just fucking destroyed you. You lost kiddo. Get over it.")))
            print("")
            type(red(bright("You lost your bet of " + green("$" + str(bet)))))
            print("\n")
            type(red(bright("Your new balance is " + green("$" + str(balance) + red(" - $" + str(bet)) + green(" = $" + str((balance - bet)))))))
            print("")
            return balance-bet

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
                additional_card_value = check_value(additional_card)
                additional_card_suit = check_suit(additional_card)
                if (additional_card_value == "Ace") or (additional_card_value == "Eight"):
                  type("Your next card is an " + magenta(bright( additional_card_value + " " + additional_card_suit)))
                else:
                  type("Your next card is a " + magenta(bright( additional_card_value + " " + additional_card_suit)))
                  
                print("")

                additional_card_int, ace = card_int(additional_card, ace)
                current_hand_int = current_hand_int + additional_card_int

                print_hand_value(current_hand_int, ace)

                game_over = check_value_21_or_over(current_hand_int, ace)

                if game_over == "Bust":
                    print("")
                    type(red(bright("You went over 21! Bust! You Lose!")))
                    print("")
                    type(red(bright("You lost your bet of " + green("$" + str(bet)))))
                    print("\n")
                    type(red(bright("Your new balance is " + green("$" + str(balance) + red(" - $" + str(bet)) + green(" = $" + str((balance - bet)))))))
                    print("")
                    return balance-bet
                elif game_over == "Blackjack":
                    print("")
                    type(yellow(bright("You got a Blackjack! You Win! Yay!")))
                    print("")
                    type(yellow(bright("With an innital bet of " + green("$" + str(bet)) + yellow(", you've tripled it!"))))
                    print("\n")
                    type(yellow(bright("Your new balance is " + green("$" + str(balance) + " + $" + str(bet*2) + " = $" + str(balance+(2*bet))))))
                    print("")
                    return balance + (2*bet)

            elif (decisions_decisions == "STAND") or (decisions_decisions == "S"):

                if (ace > 0) & (current_hand_int + 10 < 21):
                    current_hand_int = current_hand_int + 10
                type("You decided to stand at a value of ", green(bright(str(current_hand_int))))
                print("\n")

                if ((dealer_card_two_value == "Ace") or (dealer_card_two_value == "Eight")):
                    type(red("The dealer's second card is an " + bright(dealer_card_two_value + " " + dealer_card_two_suit)))
                else:
                    type(red("The dealer's second card is a " + bright(dealer_card_two_value + " " + dealer_card_two_suit)))

                print("")

                print_dealer_hand_value(dealer_current_hand_int, dealer_ace)

                dealer_playing = 0
                while dealer_playing == 0:
                    if (21 == dealer_current_hand_int > current_hand_int):
                        type(red("The dealer stands at " + bright(str(dealer_current_hand_int))))
                        print("\n")
                        type(red(bright("The dealer gets a Blackjack and wins! Too bad! So sad! Get good, kiddo!")))
                        print("")
                        type(red(bright("You lost your bet of " + green("$" + str(bet)))))
                        print("\n")
                        type(red(bright("Your new balance is " + green("$" + str(balance) + red(" - $" + str(bet)) + green(" = $" + str((balance - bet)))))))
                        print("")
                        return balance - bet
                    elif (21 > dealer_current_hand_int > current_hand_int):
                        type(red("The dealer stands at " + bright(str(dealer_current_hand_int))))
                        print("\n")
                        type(red(bright("The dealer wins! Too bad! So sad! Stay mad!")))
                        print("")
                        type(red(bright("You lost your bet of " + green("$" + str(bet)))))
                        print("\n")
                        type(red(bright("Your new balance is " + green("$" + str(balance) + red(" - $" + str(bet)) + green(" = $" + str((balance - bet)))))))
                        print("")
                        return balance - bet
                    elif ((dealer_ace > 0) & (21 > (dealer_current_hand_int + 10) > current_hand_int)):
                        type(red("The dealer stands at " + bright(str(dealer_current_hand_int + 10))))
                        print("\n")
                        type(red(bright("The dealer wins! Too bad! So sad! You suuuuck!")))
                        print("")
                        type(red(bright("You lost your bet of " + green("$" + str(bet)))))
                        print("\n")
                        type(red(bright("Your new balance is " + green("$" + str(balance) + red(" - $" + str(bet)) + green(" = $" + str((balance - bet)))))))
                        print("")
                        return balance - bet
                    elif ((dealer_ace > 0) & (21 == (dealer_current_hand_int + 10) > current_hand_int)):
                        print("")
                        type(red("The dealer stands at " + bright(str(dealer_current_hand_int + 10))))
                        print("\n")
                        type(red(bright("The dealer gets a Blackjack and wins! You're an embarrassment.")))
                        print("")
                        type(red(bright("You lost your bet of " + green("$" + str(bet)))))
                        print("\n")
                        type(red(bright("Your new balance is " + green("$" + str(balance) + red(" - $" + str(bet)) + green(" = $" + str((balance - bet)))))))
                        print("")
                        return balance - bet
                    elif (dealer_current_hand_int > 21):
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
                    elif ((dealer_current_hand_int >= 17)):
                        type(red("The dealer stands at " + str(dealer_current_hand_int)))
                        print("\n")
                        type(magenta(bright("Congrats! You Win! Get REKT, dealer!")))
                        print("")
                        type(magenta(bright("With an innital bet of " + green("$" + str(bet)) + magenta(", you've doubled it!"))))
                        print("\n")
                        type(magenta(bright("Your new balance is " + green("$" + str(balance) + " + $" + str(bet) + " = $" + str(balance + bet)))))
                        print("")
                        return (balance + bet)
                    elif ((dealer_ace > 0) & ((dealer_current_hand_int + 10) <= 21) & ((21 - (dealer_current_hand_int + 10))<=4)):
                        type(red("The dealer stands at " + bright(str((dealer_current_hand_int + 10)))))
                        print("\n")
                        type(magenta(bright("Congrats! You Win! Take that, dealer!")))
                        print("")
                        type(magenta(bright("With an innital bet of " + green("$" + str(bet)) + magenta(", you've doubled it!"))))
                        print("\n")
                        type(magenta(bright("Your new balance is " + green("$" + str(balance) + " + $" + str(bet) + " = $" + str(balance + bet)))))
                        print("")
                        return (balance + bet)
                    else:
                        type(red("The dealer's cards are a value under 17 so they hit"))

                        print("")

                        additional_dealer_card = deck_of_cards.pop(0)
                        additional_dealer_card_value = check_value(additional_dealer_card)
                        additional_dealer_card_suit = check_suit(additional_dealer_card)
                        if ((additional_dealer_card_value == "Ace") or (additional_dealer_card_value == "Eight")):
                            type(red("The dealer's next card is an " + bright(additional_dealer_card_value + " " + additional_dealer_card_suit)))
                        else:
                            type(red("The dealer's next card is a " + bright(additional_dealer_card_value + " " + additional_dealer_card_suit)))

                        print("")

                        additional_dealer_card_int, dealer_ace = card_int(additional_dealer_card, dealer_ace)
                        dealer_current_hand_int = dealer_current_hand_int + additional_dealer_card_int
                        print_dealer_hand_value(dealer_current_hand_int, dealer_ace)

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
                    dealer_story += 1
                elif dealer_story == 6:
                    story.dealer_tale()

    type("")

def check_balance(balance):
    return (balance <= 0) or (balance >=1000000)

def find_rank(balance, rank):
    if (balance > 0) and (balance < 1000):
        if rank == 1:
            type(red(bright("Your wallet feels smaller than it was before.")))
        return 0
    if (balance >= 1000) and balance < (balance < 10000):
        if rank == 0:
            type(green(bright("Your wallet feels larger than it was before.")))
        elif rank == 2:
            type(red(bright("Your wallet feels smaller than it was before.")))
        return 1
    if (balance >= 10000) and balance < (balance < 100000):
        if rank == 1:
            type(green(bright("Your wallet feels larger than it was before.")))
        elif rank == 3:
            type(red(bright("Your wallet feels smaller than it was before.")))
        return 2
    if (balance >= 100000) and balance < (balance < 500000):
        if rank == 2:
            type(green(bright("Your wallet feels larger than it was before.")))
        elif rank == 4:
            type(red(bright("Your wallet feels smaller than it was before.")))
        return 3
    if (balance >= 500000) and balance < (balance < 900000):
        if rank == 3:
            type(green(bright("Your wallet feels larger than it was before.")))
        elif rank == 5:
            type(red(bright("Your wallet feels smaller than it was before.")))
        return 4
    if (balance >= 900000) and balance < (balance < 1000000):
        if rank == 4:
            type(green(bright("Your wallet feels larger than it was before.")))
        return 5

def casino(balance, number_of_rounds, status_effects):
    rounds_played = 0
    while (rounds_played < number_of_rounds) and (balance > 0) and (balance < 1000000):
            bet = choose_bet(balance)
            if bet=="dead":
                return balance, False
            else:
                balance = blackjack_main(bet, balance)
                rounds_played += 1
    return balance, True, status_effects

def main():
    day_poor = story.make_random_event_list(0, 0)
    day_cheap = story.make_random_event_list(0, 1)
    day_modest = story.make_random_event_list(0, 2)
    day_rich = story.make_random_event_list(0, 3)
    day_doughman = story.make_random_event_list(0, 4)
    day_nearly_there = story.make_random_event_list(0, 5)
    night_poor = story.make_random_event_list(1, 0)
    night_cheap = story.make_random_event_list(1, 1)
    night_modest = story.make_random_event_list(1, 2)
    night_rich = story.make_random_event_list(1, 3)
    night_doughman = story.make_random_event_list(1, 4)
    night_nearly_there = story.make_random_event_list(1, 5)
    quote_list = story.make_random_event_list(-1, -1)
    status_effects = set()
    items = []
    number_of_rounds = 1
    rank = 0
    day_count = 0
    balance = 50
    previous_balance = balance
    is_alive = True
    # is_alive = story.first_setup()
    while (is_alive==True) and (balance >= 1) and (balance < 1000000):
        # story.opening_lines()
        type("Would you like to play a game of Blackjack? ")
        decisions_decisions = input("")
        decisions_decisions = decisions_decisions.upper()
        print("")
        type("You have " + green(bright("$" + str(balance))))
        
        balance, is_alive, status_effects = casino(balance, number_of_rounds, status_effects) # plays inputted number of blackjack rounds

        if check_balance(balance): # checks if balance below 0 or over 1 million, then breaks loop
            break

        if is_alive == False: # Check if alive is False
            break

        print("")

        rank = find_rank(balance, rank)

        print("")

        day_count += 1
        if day_count == 1:
            story.end_day_1()

        print("\n")

        if len(quote_list) == 0:
            quote_list = story.make_random_event_list(-1, -1)
        story.day_summary(balance, previous_balance, rank, day_count, quote_list)

        previous_balance = balance

        print("\n")

        if rank == 0:
            if len(day_poor) == 0:
                day_poor = story.make_random_event_list(0, rank)
            event = day_poor.pop()
            balance, is_alive = story.random_day_event_poor(event, balance, is_alive, status_effects, items)
        elif rank == 1:
            if len(day_cheap) == 0:
                day_cheap = story.make_random_event_list(0, rank)
            event = day_cheap.pop()
            balance, is_alive = story.random_day_event_cheap(event, balance, is_alive, status_effects, items)
        if rank == 2:
            if len(day_modest) == 0:
                day_modest = story.make_random_event_list(0, rank)
            event = day_modest.pop()
            balance, is_alive = story.random_day_event_modest(event, balance, is_alive, status_effects, items)
        elif rank == 3:
            if len(day_rich) == 0:
                day_rich = story.make_random_event_list(0, rank)
            event = day_rich.pop()
            balance, is_alive = story.random_day_event_rich(event, balance, is_alive, status_effects, items)
        elif rank == 4:
            if len(day_doughman) == 0:
                day_doughman = story.make_random_event_list(0, rank)
            event = day_doughman.pop()
            balance, is_alive = story.random_day_event_doughman(event, balance, is_alive, status_effects, items)
        elif rank == 5:
            if len(day_nearly_there) == 0:
                day_nearly_there = story.make_random_event_list(0, rank)
            event = day_nearly_there.pop()
            balance, is_alive = story.random_day_event_nearly_there(event, balance, is_alive, status_effects, items)

        print ("\n")

        if is_alive == False: # Check if alive is false
            break

        print("")

        rank = find_rank(balance, rank)

        print("\n")

        if rank == 0:
            if len(night_poor) == 0:
                night_poor = story.make_random_event_list(0, rank)
            event = night_poor.pop()
            balance, is_alive = story.random_night_event_poor(event, balance, is_alive, status_effects, items)
        elif rank == 1:
            if len(night_cheap) == 0:
                night_cheap = story.make_random_event_list(0, rank)
            event = night_cheap.pop()
            balance, is_alive = story.random_night_event_cheap(event, balance, is_alive, status_effects, items)
        if rank == 2:
            if len(night_modest) == 0:
                night_modest = story.make_random_event_list(0, rank)
            event = night_modest.pop()
            balance, is_alive = story.random_night_event_modest(event, balance, is_alive, status_effects, items)
        elif rank == 3:
            if len(night_rich) == 0:
                night_rich = story.make_random_event_list(0, rank)
            event = night_rich.pop()
            balance, is_alive = story.random_night_event_rich(event, balance, is_alive, status_effects, items)
        elif rank == 4:
            if len(night_doughman) == 0:
                night_doughman = story.make_random_event_list(0, rank)
            event = night_doughman.pop()
            balance, is_alive = story.random_night_event_doughman(event, balance, is_alive, status_effects, items)
        elif rank == 5:
            if len(night_nearly_there) == 0:
                night_nearly_there = story.make_random_event_list(0, rank)
            event = night_nearly_there.pop()
            balance, is_alive = story.random_night_event_nearly_there(event, balance, is_alive, status_effects, items)

        print("")
        type_slow("It's about time that you return to the casino. You wouldn't want to keep the dealer waiting.")
        print("")


    print("") #print before game over messages

    if is_alive == False:
        type_slow("You have died!")
        print("")
        type_slow("You met your fate with a final balance of " + green(bright("$" + str(balance))))
        print("")
        type_slow("The police were able to recover your body, but nobody cared enough to show at your funeral.")

    if balance < 1:
        type_slow("You have run out of money!")
        print("")
        type_slow("With no cash left to play Blackjack, your source of income has been rendered useless.")
        print("")
        type_slow("You spend your remaining days going hungry, wondering what life could've been, if you didn't hit that one hand.")
    
    if balance >= 1000000:
        type_slow("u win lol look at u millionaire go girl")

main()