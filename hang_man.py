import random

print("Welcome To Hang Man")


def words_picker():
    f = open("words.txt", "r")
    words = f.readlines()
    words = [x.strip() for x in words]
    pick_word = random.choice(words)
    f.close()
    return pick_word


def hang_man():
    result = 0  # something is wrong if return 0
    start = input("Do you want to start the game Y/N ?").lower()
    attemps = 10
    chosen_word = words_picker()
    if start != "y":
        result = 2
    else:
        blank = "_" * len(chosen_word)
        print(f"This word have {len(chosen_word)} characters: {blank}")
        while attemps > 0:
            guess = input("What is your guest (one word at a time only)?").lower()
            if len(guess) != 1:
                print("Please guess one letter at a time!")
                continue
            elif guess in chosen_word:
                if guess in blank:
                    print("You already enter that letter")
                    attemps -= 1
                    print(f"You have {attemps} attempts left.")
                else:
                    print("that correct")
                    blank = string_correction(guess, chosen_word, blank)
                    print(f"Current word {blank}")
            elif guess not in chosen_word:
                attemps -= 1
                print(f"Wrong guess. You have {attemps} attempts left.")

            if "_" not in blank:
                result = 1
                break

            if attemps == 0:
                result = 2
                break

    return result, chosen_word


def string_correction(guess, chosen_word, blank):
    index = 0
    blank_space = ""
    blank_updated = blank

    while index < len(chosen_word):
        if chosen_word[index] == guess:
            blank_space += guess
        else:
            blank_space += blank_updated[index]
        index += 1
    blank_updated = blank_space
    return blank_updated


def game_result(game_result, chosen_word):
    res = 0
    if game_result == 1:
        print("Congratulations, you've guessed the word!")
        res = 1
    elif game_result == 2:
        print(f"Game over! The word was: {chosen_word}")
    elif game_result == 0:
        print("Something is wrong with the function hang_man()!")
    else:
        raise ValueError(f"Action not defined for result value {chosen_word}")

    return res


if __name__ == "__main__":
    print("Start game hangman")
    res, chosen_word = hang_man()
    game_result(res, chosen_word)
    print(f"Game is done! Result value is: {res}")
