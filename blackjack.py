import random
from colorama import Fore, Back, Style
import time
import random
import sys
import story

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
        fancy_type("Your cards have a value of ", green_text(bright_text(str(hand_value))) + ", or " + green_text(bright_text(str((hand_value + 10)))) + " since you have an ace")
        print("")
    elif (ace > 0) & ((hand_value + 10) == 21):
        fancy_type("Your cards have a value of ", green_text(bright_text(str(hand_value + 10))))
    else:
        fancy_type("Your cards have a value of ", green_text(bright_text(str(hand_value))))
        print("")

def print_dealer_hand_value(dealer_hand_value, dealer_ace):
    if (dealer_ace > 0) & ((dealer_hand_value + 10) < 21):
        fancy_type(red_text("The dealer's cards have a value of " + bright_text(str((dealer_hand_value))) + ", or " + bright_text( str((dealer_hand_value + 10))) + " since they have an ace"))
        print("\n")
    elif (dealer_ace > 0) & ((dealer_hand_value + 10) == 21):
        fancy_type(red_text("The dealer's cards have a value of " + bright_text(str((dealer_hand_value + 10)))))
    else:
        fancy_type(red_text("The dealer's cards have a value of " + bright_text(str((dealer_hand_value)))))
        print("\n")

def is_value_21_or_over(value, ace):
    if value == 21:
        return "Blackjack"
    elif (ace>0) & (value+10==21):
        return "Blackjack"
    elif value > 21:
        return "Bust"
    else:
        return
    
def choose_bet(balance):
    print("")
    currently_betting = 1
    angry_dealer=0
    while currently_betting != 0:
        bet = None
        while bet is None:
            fancy_type("How much would you like to bet? ")
            try:
                bet = int(input(""))
            except ValueError:
                print("")
                fancy_type(red_text("The dealer looks at you confused. Perhaps he didn't hear you."))
                print("\n")

        print("")
        if(int(bet)<=balance) and (int(bet)>0):
            balance = balance-bet
            return int(bet), balance
        elif((int(bet)==0) and (angry_dealer==0)):
            fancy_type_slow(red_text("The dealer looks at you with an aggressive eye. Maybe try betting some cash!"))
            print("\n")
            angry_dealer += 1
        elif((int(bet)==0) and (angry_dealer==1)):
            fancy_type_slow(red_text("The dealer is infuriated. You've insulted him. You should bet some cash."))
            print("\n")
            angry_dealer += 1
        elif((int(bet)==0) and (angry_dealer==2)):
            fancy_type_slow(red_text("The dealer gets up from his chair and charges his relover. Bet some cash. You'll regret it if you don't."))
            print("\n")
            angry_dealer += 1
        elif((int(bet)==0) and (angry_dealer==3)):
            fancy_type_slow(red_text("The dealer fires three shots into your chest. You bleed out, and as you fade from reality, you see the dealer reach into your pockets, and take every last penny from your lifeless body."))
            return "dead"
        else:
            fancy_type(red_text("The dealer looks at you confused. Perhaps he didn't hear you."))
            print("\n")


def blackjack_main(bet, balance):
    game_running = 1
    while game_running == 1:
        deck_of_cards = shuffle_cards()
        card_one = deck_of_cards.pop(0)
        card_one_value = check_value(card_one)
        card_one_suit = check_suit(card_one)

        if ((card_one_value == "Ace") or (card_one_value == "Eight")):
            fancy_type("Your first card is an ", magenta_text(bright_text(card_one_value + " " + card_one_suit)))
        else:
            fancy_type("Your first card is a ", magenta_text(bright_text(card_one_value + " " + card_one_suit)))

        print("")

        dealer_card_one = deck_of_cards.pop(0)
        dealer_card_one_value = check_value(dealer_card_one)
        dealer_card_one_suit = check_suit(dealer_card_one)

        if ((dealer_card_one_value == "Ace") or (dealer_card_one_value == "Eight")):
            fancy_type(red_text("The dealer's first card is an " + bright_text(dealer_card_one_value + " " + dealer_card_one_suit)))
        else:
            fancy_type(red_text("The dealer's first card is a " + bright_text(dealer_card_one_value + " " + dealer_card_one_suit)))
        
        print("\n")

        card_two = deck_of_cards.pop(0)
        card_two_value = check_value(card_two)
        card_two_suit = check_suit(card_two)
        if ((card_two_value == "Ace") or (card_two_value == "Eight")):
            fancy_type("Your second card is an " + magenta_text(bright_text(card_two_value + " " + card_two_suit)))
        else:
            fancy_type("Your second card is a " + magenta_text(bright_text(card_two_value + " " + card_two_suit)))
            
        print("")

        dealer_card_two = deck_of_cards.pop(0)
        dealer_card_two_value = check_value(dealer_card_two)
        dealer_card_two_suit = check_suit(dealer_card_two)
        
        dealer_ace = 0
        card_int_check = card_int(dealer_card_one, dealer_ace)
        dealer_card_one_int = card_int_check[0]
        dealer_ace = card_int_check[1]

        card_int_check = card_int(dealer_card_two, dealer_ace)
        dealer_card_two_int = card_int_check[0]
        dealer_ace = card_int_check[1]

        dealer_current_hand_int = dealer_card_one_int + dealer_card_two_int
        is_game_over_dealer = is_value_21_or_over(dealer_current_hand_int, dealer_ace)
        if is_game_over_dealer == "Blackjack":
            if ((dealer_card_two_value == "Ace")):
                fancy_type(red_text("The dealer's second card is an " + bright_text(dealer_card_two_value + " " + dealer_card_two_suit)))
                print("")
                fancy_type(red_text("The dealer's cards have a value of 21 ;)"))
            else:
                fancy_type(red_text("The dealer's second card is a " + bright_text(dealer_card_two_value + " " + dealer_card_two_suit)))
                print("")
                fancy_type(red_text("The dealer's cards have a value of 21 ;)"))
        else:
            fancy_type(red_text("The dealer's second card is face down"))
            
        print("")
        
        # prints dealer's starting value
        if is_game_over_dealer != "Blackjack":
            if dealer_card_one_int == 1:
                print("")
                fancy_type(red_text("As of now, the dealer's cards have a known value of " + bright_text("1") + " or " + bright_text("11") + ", since they have an ace"))
            else:    
                print("")
                fancy_type(red_text("As of now, the dealer's cards have a known value of " + bright_text(str(dealer_card_one_int))))

        print("")

        ace = 0
        response = 0

        card_int_check = card_int(card_one, ace)
        card_one_int = card_int_check[0]
        ace = card_int_check[1]

        card_int_check = card_int(card_two, ace)
        card_two_int = card_int_check[0]
        ace = card_int_check[1]

        current_hand_int = card_one_int + card_two_int

        print_hand_value(current_hand_int, ace)

        is_game_over = is_value_21_or_over(current_hand_int, ace)

        if is_game_over == "Bust":
            print("\n")
            fancy_type(red_text(bright_text("You went over 21! Bust! You Lose!")))
            print("")
            fancy_type(red_text(bright_text("You lost your bet of " + green_text("$" + str(bet)))))
            print("\n")
            fancy_type(red_text(bright_text("Your new balance is " + green_text("$" + str(balance)))))
            print("")
            return balance
        elif (is_game_over == "Blackjack") & (is_game_over_dealer == "Blackjack"):
            print("\n")
            fancy_type(cyan_text(bright_text("You and the dealer both got a Blackjack. How boring.")))
            print("")
            fancy_type(cyan_text(bright_text("You win back your bet of " + green_text("$" + str(bet)))))
            print("\n")
            fancy_type(cyan_text(bright_text("Your balance has returned to " + green_text("$" + str(balance)))))
            print("")
            balance += bet
            return balance
        elif is_game_over == "Blackjack":
            print("\n")
            fancy_type(yellow_text(bright_text("You got a Blackjack! You Win! Huzzah! Bon Voyage!")))
            print("")
            fancy_type(yellow_text(bright_text("With an innital bet of " + green_text("$" + str(bet)) + yellow_text(", you've tripled it!"))))
            print("\n")
            fancy_type(yellow_text(bright_text("Your new balance is " + green_text("$" + str(balance) + " + $" + str(bet*3) + " = $" + str(balance+(3*bet))))))
            print("")
            balance += (bet*3)
            return balance
        elif is_game_over_dealer == "Blackjack":
            print("")
            fancy_type(red_text(bright_text("Damn the dealer just fucking destroyed you. You lost kiddo. Get over it.")))
            print("")
            fancy_type(red_text(bright_text("You lost your bet of " + green_text("$" + str(bet)))))
            print("\n")
            fancy_type(red_text(bright_text("Your new balance is " + green_text("$" + str(balance)))))
            print("")
            return balance

        # Gameplay loop (Hitting repeatedly, then dealer hitting repeatedly)
        while response == 0:
            fancy_type("Would you like to hit or stand? ")
            decisions_decisions = input ('')
            print("") # Prints a line for spacing purposes
            decisions_decisions = decisions_decisions.upper()

            if (decisions_decisions == "HIT") or (decisions_decisions == "H"):
                additional_card = deck_of_cards.pop(0)
                additional_card_value = check_value(additional_card)
                additional_card_suit = check_suit(additional_card)
                if (additional_card_value == "Ace") or (additional_card_value == "Eight"):
                  fancy_type("Your next card is an " + magenta_text(bright_text( additional_card_value + " " + additional_card_suit)))
                else:
                  fancy_type("Your next card is a " + magenta_text(bright_text( additional_card_value + " " + additional_card_suit)))
                  
                print("")

                card_int_check = card_int(additional_card, ace)
                additional_card_int = card_int_check[0]
                ace = card_int_check[1]
                current_hand_int = current_hand_int + additional_card_int
                print_hand_value(current_hand_int, ace)

                is_game_over = is_value_21_or_over(current_hand_int, ace)

                if is_game_over == "Bust":
                    print("")
                    fancy_type(red_text(bright_text("You went over 21! Bust! You Lose!")))
                    print("")
                    fancy_type(red_text(bright_text("You lost your bet of " + green_text("$" + str(bet)))))
                    print("\n")
                    fancy_type(red_text(bright_text("Your new balance is " + green_text("$" + str(balance)))))
                    print("")
                    return balance
                elif is_game_over == "Blackjack":
                    print("")
                    fancy_type(yellow_text(bright_text("You got a Blackjack! You Win! Yay!")))
                    print("")
                    fancy_type(yellow_text(bright_text("With an innital bet of " + green_text("$" + str(bet)) + yellow_text(", you've tripled it!"))))
                    print("\n")
                    fancy_type(yellow_text(bright_text("Your new balance is " + green_text("$" + str(balance) + " + $" + str(bet*3) + " = $" + str(balance+(3*bet))))))
                    print("")
                    balance += (bet*3)
                    return balance

            elif (decisions_decisions == "STAND") or (decisions_decisions == "S"):

                if (ace > 0) & (current_hand_int + 10 < 21):
                    current_hand_int = current_hand_int + 10
                fancy_type("You decided to stand at a value of ", green_text(bright_text(str(current_hand_int))))
                print("\n")

                if ((dealer_card_two_value == "Ace") or (dealer_card_two_value == "Eight")):
                    fancy_type(red_text("The dealer's second card is an " + bright_text(dealer_card_two_value + " " + dealer_card_two_suit)))
                else:
                    fancy_type(red_text("The dealer's second card is a " + bright_text(dealer_card_two_value + " " + dealer_card_two_suit)))

                print("")

                print_dealer_hand_value(dealer_current_hand_int, dealer_ace)

                dealer_playing = 0
                while dealer_playing == 0:
                    if (21 == dealer_current_hand_int > current_hand_int):
                        fancy_type(red_text("The dealer stands at " + bright_text(str(dealer_current_hand_int))))
                        print("\n")
                        fancy_type(red_text(bright_text("The dealer gets a Blackjack and wins! Too bad! So sad! Get good, kiddo!")))
                        print("")
                        fancy_type(red_text(bright_text("You lost your bet of " + green_text("$" + str(bet)))))
                        print("\n")
                        fancy_type(red_text(bright_text("Your new balance is " + green_text("$" + str(balance)))))
                        print("")
                        return balance
                    elif (21 > dealer_current_hand_int > current_hand_int):
                        fancy_type(red_text("The dealer stands at " + bright_text(str(dealer_current_hand_int))))
                        print("\n")
                        fancy_type(red_text(bright_text("The dealer wins! Too bad! So sad! Stay mad!")))
                        print("")
                        fancy_type(red_text(bright_text("You lost your bet of " + green_text("$" + str(bet)))))
                        print("\n")
                        fancy_type(red_text(bright_text("Your new balance is " + green_text("$" + str(balance)))))
                        print("")
                        return balance
                    elif ((dealer_ace > 0) & (21 > (dealer_current_hand_int + 10) > current_hand_int)):
                        fancy_type(red_text("The dealer stands at " + bright_text(str(dealer_current_hand_int + 10))))
                        print("\n")
                        fancy_type(red_text(bright_text("The dealer wins! Too bad! So sad! You suuuuck!")))
                        print("")
                        fancy_type(red_text(bright_text("You lost your bet of " + green_text("$" + str(bet)))))
                        print("\n")
                        fancy_type(red_text(bright_text("Your new balance is " + green_text("$" + str(balance)))))
                        print("")
                        return balance
                    elif ((dealer_ace > 0) & (21 == (dealer_current_hand_int + 10) > current_hand_int)):
                        print("")
                        fancy_type(red_text("The dealer stands at " + bright_text(str(dealer_current_hand_int + 10))))
                        print("\n")
                        fancy_type(red_text(bright_text("The dealer gets a Blackjack and wins! You're an embarrassment.")))
                        print("")
                        fancy_type(red_text(bright_text("You lost your bet of " + green_text("$" + str(bet)))))
                        print("\n")
                        fancy_type(red_text(bright_text("Your new balance is " + green_text("$" + str(balance)))))
                        print("")
                        return balance
                    elif (dealer_current_hand_int > 21):
                        fancy_type(magenta_text(bright_text("The dealer went over 21! Bust! You Win!")))
                        print("")
                        fancy_type(magenta_text(bright_text("With an innital bet of " + green_text("$" + str(bet)) + magenta_text(", you've doubled it!"))))
                        print("\n")
                        fancy_type(magenta_text(bright_text("Your new balance is " + green_text("$" + str(balance) + " + $" + str(bet*2) + " = $" + str(balance+(2*bet))))))
                        print("")
                        balance += (bet*2)
                        return balance
                    elif (dealer_current_hand_int == current_hand_int):
                        fancy_type(red_text("The dealer stands at " + bright_text(str(dealer_current_hand_int))))
                        print("\n")
                        fancy_type(cyan_text(bright_text("Since you and the dealer have the same value, it's a draw. So, so very lame.")))
                        print("")
                        fancy_type(cyan_text(bright_text("You win back your bet of " + green_text("$" + str(bet)))))
                        print("\n")
                        fancy_type(cyan_text(bright_text("Your balance has returned to " + green_text("$" + str(balance)))))
                        print("")
                        balance += bet
                        return balance
                    elif ((dealer_current_hand_int >= 17)):
                        fancy_type(red_text("The dealer stands at " + str(dealer_current_hand_int)))
                        print("\n")
                        fancy_type(magenta_text(bright_text("Congrats! You Win! Get REKT, dealer!")))
                        print("")
                        fancy_type(magenta_text(bright_text("With an innital bet of " + green_text("$" + str(bet)) + magenta_text(", you've doubled it!"))))
                        print("\n")
                        fancy_type(magenta_text(bright_text("Your new balance is " + green_text("$" + str(balance) + " + $" + str(bet*2) + " = $" + str(balance+(2*bet))))))
                        print("")
                        balance += (bet*2)
                        return balance
                    elif ((dealer_ace > 0) & ((dealer_current_hand_int + 10) <= 21) & ((21 - (dealer_current_hand_int + 10))<=4)):
                        fancy_type(red_text("The dealer stands at " + bright_text(str((dealer_current_hand_int + 10)))))
                        print("\n")
                        fancy_type(magenta_text(bright_text("Congrats! You Win! Take that, dealer!")))
                        print("")
                        fancy_type(magenta_text(bright_text("With an innital bet of " + green_text("$" + str(bet)) + magenta_text(", you've doubled it!"))))
                        print("\n")
                        fancy_type(magenta_text(bright_text("Your new balance is " + green_text("$" + str(balance) + " + $" + str(bet*2) + " = $" + str(balance+(2*bet))))))
                        print("")
                        balance += (bet*2)
                        return balance
                    else:
                        fancy_type(red_text("The dealer's cards are a value under 17 so they hit"))

                        print("")

                        additional_dealer_card = deck_of_cards.pop(0)
                        additional_dealer_card_value = check_value(additional_dealer_card)
                        additional_dealer_card_suit = check_suit(additional_dealer_card)
                        if ((additional_dealer_card_value == "Ace") or (additional_dealer_card_value == "Eight")):
                            fancy_type(red_text("The dealer's next card is an " + bright_text(additional_dealer_card_value + " " + additional_dealer_card_suit)))
                        else:
                            fancy_type(red_text("The dealer's next card is a " + bright_text(additional_dealer_card_value + " " + additional_dealer_card_suit)))

                        print("")

                        dealer_card_int_check = card_int(additional_dealer_card, dealer_ace)
                        additional_dealer_card_int = dealer_card_int_check[0]
                        dealer_ace = dealer_card_int_check[1]
                        dealer_current_hand_int = dealer_current_hand_int + additional_dealer_card_int
                        print_dealer_hand_value(dealer_current_hand_int, dealer_ace)

            else:
                fancy_type("I'm sorry, I didn't get that. Could you speak up?")
                print("\n")

    fancy_type("")


def main():
    balance = 50
    alive = 1
    bankrupt = 1
    millionaire = 1
    # alive = story.first_setup()
    while (alive==1) and (bankrupt==1) and (millionaire == 1):
        # story.opening_lines()
        fancy_type("Would you like to play a game of Blackjack? ")
        decisions_decisions = input("")
        decisions_decisions = decisions_decisions.upper()
        rounds = 0
        print("")
        fancy_type("Your current balance is " + green_text(bright_text("$" + str(balance))))
        while rounds != 3:
            taking_bets = choose_bet(balance)
            bet = taking_bets[0]
            balance = taking_bets[1]
            if bet==0:
                alive == 0
                break
            else:
                balance = blackjack_main(bet, balance)
                rounds += 1
        
        print("")
        story.end_day_1()

main()