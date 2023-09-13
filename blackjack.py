import random
import array

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
        print("Your cards have a value of ", (hand_value), ", or ", (hand_value + 10), " since you have an ace", sep="", end="\n \n")
    elif (ace > 0) & ((hand_value + 10) == 21):
        print("Your cards have a value of", (hand_value + 10))
    else:
        print("Your cards have a value of", (hand_value), end="\n \n")

def print_dealer_hand_value(dealer_hand_value, dealer_ace):
    if (dealer_ace > 0) & ((dealer_hand_value + 10) < 21):
        print("The dealer's cards have a value of ", (dealer_hand_value), ", or ", (dealer_hand_value + 10), " since they have an ace", sep="", end="\n \n")
    elif (dealer_ace > 0) & ((dealer_hand_value + 10) == 21):
        print("The dealer's cards have a value of", (dealer_hand_value + 10))
    else:
        print("The dealer's cards have a value of", (dealer_hand_value), end="\n \n")

def is_value_21_or_over(value, ace):
    if value == 21:
        return "Blackjack"
    elif (ace>0) & (value+10==21):
        return "Blackjack"
    elif value > 21:
        return "Bust"
    else:
        return
    
def main():
    input("Would you like to play a game? ")
    print("")
    game_running = 1
    while game_running == 1:
        deck_of_cards = shuffle_cards()
        card_one = deck_of_cards.pop(0)
        card_one_value = check_value(card_one)
        card_one_suit = check_suit(card_one)
        print("Your first card is a", card_one_value, card_one_suit)

        dealer_card_one = deck_of_cards.pop(0)
        dealer_card_one_value = check_value(dealer_card_one)
        dealer_card_one_suit = check_suit(dealer_card_one)
        print("The dealer's first card is a", dealer_card_one_value, dealer_card_one_suit, end="\n \n")

        card_two = deck_of_cards.pop(0)
        card_two_value = check_value(card_two)
        card_two_suit = check_suit(card_two)
        print("Your second card is a", card_two_value, card_two_suit)

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
            print("The dealer's second card is", dealer_card_two_value, dealer_card_two_suit)
            print("The dealer's cards have a value of 21 ;)")
        else:
            print("The dealer's second card is face down", end = "\n \n")
        
        # prints dealer's starting value
        if dealer_card_one_int == 1:
            print("As of now, the dealer's cards have a known value of 1 or 11, since they have an ace")
        else:    
            print("As of now, the dealer's cards have a known value of", dealer_card_one_int)

        ace = 0

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
            print("You went over 21! Bust! You Lose!")
            game_running=0
        elif (is_game_over == "Blackjack") & (is_game_over_dealer == "Blackjack"):
            print("You and the dealer both got a Blackjack. How boring.")
            game_running=0
        elif is_game_over == "Blackjack":
            print("You got a Blackjack! You Win! Yay!")
            game_running=0
        elif is_game_over_dealer == "Blackjack":
            print("Damn the dealer just fucking destroyed you. You lost kiddo. Get over it.")
            game_running=0

        # Gameplay loop (Hitting repeatedly, then dealer hitting repeatedly)
        response = 0
        while response == 0:
            decisions_decisions = input ("Would you like to hit or stand? ")
            print("") # Prints a line for spacing purposes
            decisions_decisions = decisions_decisions.upper()

            if decisions_decisions == "HIT":
                additional_card = deck_of_cards.pop(0)
                additional_card_value = check_value(additional_card)
                additional_card_suit = check_suit(additional_card)
                print("Your next card is a", additional_card_value, additional_card_suit)

                card_int_check = card_int(additional_card, ace)
                additional_card_int = card_int_check[0]
                ace = card_int_check[1]

                current_hand_int = current_hand_int + additional_card_int

                print_hand_value(current_hand_int, ace)

                is_game_over = is_value_21_or_over(current_hand_int, ace)

                if is_game_over == "Bust":
                    print("You went over 21! Bust! You Lose!")
                    game_running=0
                elif is_game_over == "Blackjack":
                    print("You got a Blackjack! You Win! Yay!")
                    game_running=0

            elif decisions_decisions == "STAND":
                if (ace > 0) & (current_hand_int + 10 < 21):
                    current_hand_int = current_hand_int + 10
                print("You decided to stand at a value of", current_hand_int, end="\n \n")
                print("The dealer's second card is a", dealer_card_two_value, dealer_card_two_suit)
                print_dealer_hand_value(dealer_current_hand_int, dealer_ace)
                dealer_playing = 0
                while dealer_playing == 0:
                    if (21 >= dealer_current_hand_int > current_hand_int):
                        print("The dealer wins! Too bad! So sad!")
                        dealer_playing=1
                        response=1
                        game_running=0
                    elif ((dealer_ace > 0) & (21 >= (dealer_current_hand_int + 10) > current_hand_int)):
                        print("The dealer wins! Too bad! So sad!")
                        dealer_playing=1
                        response=1
                        game_running=0
                    elif (dealer_current_hand_int > 21):
                        print("The dealer went over 21! Bust! You Win!")
                        dealer_playing=1
                        response=1
                        game_running=0
                    elif ((dealer_current_hand_int >= 17)):
                        print("The dealer stays at ", dealer_current_hand_int, " and you win!", sep="")
                        dealer_playing=1
                        response=1
                        game_running=0
                    elif (dealer_ace > 0 & (21 >= (dealer_current_hand_int + 10) >= 17)):
                        print("The dealer stays at ", (dealer_current_hand_int + 10), " and you win!", sep="")
                        dealer_playing=1
                        response=1
                        game_running=0
                    else:
                        print("The dealer's cards are a value under 17 so they hit")
                        additional_dealer_card = deck_of_cards.pop(0)
                        additional_dealer_card_value = check_value(additional_dealer_card)
                        additional_dealer_card_suit = check_suit(additional_dealer_card)
                        print("The dealer's next card is a", additional_dealer_card_value, additional_dealer_card_suit)

                        dealer_card_int_check = card_int(additional_dealer_card, dealer_ace)
                        additional_dealer_card_int = dealer_card_int_check[0]
                        dealer_ace = dealer_card_int_check[1]
                        dealer_current_hand_int = dealer_current_hand_int + additional_dealer_card_int
                        print_dealer_hand_value(dealer_current_hand_int, dealer_ace)

            else:
                print("I'm sorry, I didn't get that. Could you speak up?")

    print("")

main()