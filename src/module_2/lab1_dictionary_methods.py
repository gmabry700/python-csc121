'''Dictionary Functions'''

WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")
    print("Here are yesterday's answers:")
    for word, points in WORDS.items():
        print(f"{word} was worth {points} points.")

    # print("Your letters are: A I P C R H G")
    #
    # score = 0
    # while len(WORDS) > 0:
    #     print(f"{len(WORDS)} words left!")
    #     guess = input("Guess a word: ")
    #
    #     #TODO: Check if guess in dictionary
    #     if guess == "GRAPHIC":
    #         WORDS.clear()
    #         print("You've won!")
    #     if guess in WORDS.keys():
    #         points = WORDS.pop(guess)
    #         score = score + points
    #         print(f"Good job! You scored {points} points.")
    #
    # print("That's the game!")
    # print(f"You scored {score} points!")

main()