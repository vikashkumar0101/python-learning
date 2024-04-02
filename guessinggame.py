from random import randint

EASY_LEVEL_TERMS = 10
HARD_LEVEL_TERMS = 5



def check_answer(guess, answer, turns):
    """Checks answer against guess. returns the number of turns remaining"""
    if guess > answer:
        print("Too high")
        return turns-1
    elif guess < answer:
        print("too low")
        return turns-1
    else:
        print(f"You got it! the answer is {answer}")

def set_difficulty():
    level = input("Choose a difficulty 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL_TERMS
    else:
        return HARD_LEVEL_TERMS


def game():

    print("welcome to the number  guessing game")
    print("i'm thinking a number between 1 and 100")
    answer = randint(1, 100)
    print(f"The correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts to guess the number")
        guess = int(input("Make a guess"))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, You lose.")
            return
        elif guess != answer:
            print("Guess again")

game()