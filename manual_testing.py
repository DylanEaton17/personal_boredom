import story

def test_day_summary():
    quote_list = story.make_random_event_list(-1, -1)
    balance = 61
    previous_balance = 50
    rank = 0
    day_count = 1

    story.day_summary(balance, previous_balance, rank, day_count, quote_list)

    balance = 1900
    previous_balance = 1700
    rank = 1
    day_count = 3
    print("\n")

    story.day_summary(balance, previous_balance, rank, day_count, quote_list)

    balance = 82265
    previous_balance = 78653
    rank = 2
    day_count = 8
    print("\n")

    story.day_summary(balance, previous_balance, rank, day_count, quote_list)

    balance = 104000
    previous_balance = 104000
    rank = 3
    day_count = 12
    print("\n")

    story.day_summary(balance, previous_balance, rank, day_count, quote_list)

    balance = 655777
    previous_balance = 660000
    rank = 4
    day_count = 17
    print("\n")

    story.day_summary(balance, previous_balance, rank, day_count, quote_list)

    balance = 988738
    previous_balance = 960000
    rank = 5
    day_count = 26
    print("\n")

    story.day_summary(balance, previous_balance, rank, day_count, quote_list)

def test_day_event_poor_1():
    event = 1
    balance = 50
    is_alive = True
    status_effects = []
    items = []
    story.random_day_event_poor(event, balance, is_alive, status_effects, items)
    print("\n")
    print("Event Number:", event, "Balance:", balance, "Is_alive", is_alive, status_effects, items, sep="\n")

def test_day_event_poor_2():
    event = 2
    balance = 50
    is_alive = True
    status_effects = []
    items = []
    story.random_day_event_poor(event, balance, is_alive, status_effects, items)
    print("\n")
    print("Event Number:", event, "Balance:", balance, "Is Alive:", is_alive, status_effects, items, sep="\n")

def test_drunk_blackjack():
    bet = 20
    balance = 50
    balance = story.drunk_blackjack(bet, balance)
    print(balance)

test_day_summary()
# test_day_event_poor_1()
# test_day_event_poor_2()
# test_drunk_blackjack()