import random


def deal_cards():
    """Return a random card from a deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and calculate and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw :)"
    elif computer_score == 0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You went over, lose"
    elif computer_score > 21:
        return "Computer went over, You won"
    elif user_score > computer_score:
        return "You won"
    else:
        return "You lose"


def play_again():
    user_cards = []
    computers_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computers_cards.append(deal_cards())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computers_cards)
        print(f"Your cards: {user_cards}, current score:{user_score}")
        print(f"Computer's  first card: {computers_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'Y' or 'y' to get another card or type 'n' tp pass: ")
            if user_should_deal == "Y" or "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computers_cards.append(deal_cards())
        computer_score = calculate_score(computers_cards)

    print(f"Your final hand is: {user_cards} and your final score is: {user_score}")
    print(f"Computer's final hand is: {computers_cards} and computer's final score is {computer_score}")
    print(compare(user_score, computer_score))


while (input("Do you want to play the game again if yes then type 'Y' or 'y'")) == "Y" or "y":
    play_again()
