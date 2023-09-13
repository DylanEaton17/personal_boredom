import random
import array

def shuffle_cards():
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
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
    if ace == 0:
        print("Your cards have a value of", (hand_value), end="\n \n")
    elif (ace == 1) & ((hand_value + 10) < 21):
        print("Your cards have a value of ", (hand_value), ", or ", (hand_value + 10), " since you have an ace", sep="", end="\n \n")
    elif (ace == 2) & ((hand_value + 20) < 21):
        print("Your cards have a value of ", (hand_value), ", ", (hand_value + 10), ", or, ", (hand_value + 20), " since you have two aces", sep="", end="\n \n")
    else:
        print("Your cards have a value of", (hand_value), end="\n \n")

def is_value_21_or_over(value):
    if value == 21:
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
        """
            print(deck_of_cards)
            x=0
            for x in range (0,52):
                card = deck_of_cards[x]
                card_value = check_value(card)
                card_suit = check_suit(card)
                print(card_value, card_suit)
            """

        card_one = deck_of_cards.pop(0)
        card_one_value = check_value(card_one)
        card_one_suit = check_suit(card_one)
        print("Your first card is a", card_one_value, card_one_suit)

        card_two = deck_of_cards.pop(0)
        card_two_value = check_value(card_two)
        card_two_suit = check_suit(card_two)
        print("Your second card is a", card_two_value, card_two_suit)

        ace = 0

        card_int_check = card_int(card_one, ace)
        card_one_int = card_int_check[0]
        ace = card_int_check[1]

        card_int_check = card_int(card_two, ace)
        card_two_int = card_int_check[0]
        ace = card_int_check[1]

        current_hand_int = card_one_int + card_two_int

        print_hand_value(current_hand_int, ace)

        is_game_over = is_value_21_or_over(current_hand_int)
        if is_game_over == "Bust":
            print("You went over 21! Bust! You Lose!")
            break
        elif is_game_over == "Blackjack":
            print("You got a Blackjack! You Win! Yay!")
            break

        response = 0
        while response == 0:
            decisions_decisions = input ("Would you like to hit or stay? ")
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

                is_game_over = is_value_21_or_over(current_hand_int)
                if is_game_over == "Bust":
                    print("You went over 21! Bust! You Lose!")
                    game_running=0
                    break
                elif is_game_over == "Blackjack":
                    print("You got a Blackjack! You Win! Yay!")
                    game_running=0
                    break

            elif decisions_decisions == "STAY":
                game_running = 0
                print("Well there's no dealer here at the moment so ig we're done here")
                break

            else:
                print("I'm sorry, I didn't get that. Could you speak up?")

        if current_hand_int >= 21:
            break
main()