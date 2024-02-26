import blackjackRewritten

def test_deck_len():
    # Setup
    deck = blackjackRewritten.Deck()
    expected = 52

    # Invoke
    actual = len(deck)

    # Analyze
    assert actual == expected

def test_card_repr():
    # Setup
    name = "Ace"
    suit = "Spades"
    value = 1
    card = blackjackRewritten.Card(name, suit, value)
    expected = "Ace of Spades"

    # Invoke
    actual = repr(card)

    # Analyze
    assert actual == expected