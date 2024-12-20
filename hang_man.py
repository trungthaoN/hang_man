import random
import os
from ASCII_ART import HANGMAN_ART, Welcome_art, Game_Over_art, Congrat_art


def words_picker():
    f = open("words.txt", "r")
    words = f.readlines()
    words = [x.strip() for x in words]
    pick_word = random.choice(words)
    f.close()
    return pick_word


def hang_man():
    chosen_word = words_picker()
    start = input("\033[32mDo you want to start the game Y/N ?\033[0m").lower()
    clear_console()
    if start != "y":
        return 2, chosen_word
    attempts = 9
    blank = "_" * len(chosen_word)
    print(
        f"\033[32mThis word has {len(chosen_word)} characters: {blank}\033[0m")
    print(f"\033[34m{HANGMAN_ART[0]}\033[0m")
    result = game_play(chosen_word, attempts, blank)
    return result, chosen_word


def game_play(chosen_word, attempts, blank):
    wrong_attempts = 0
    while attempts > 0 and "_" in blank:
        guess = input(
            "\033[32mWhat is your guess (one letter at a time only)?\033[0m").lower()
        clear_console()
        if len(guess) != 1:
            print("Please guess one letter at a time!")
            continue

        if guess in chosen_word:
            if guess in blank:
                print("That letter is already in the words")
                print(f"You have {attempts} attempts left.")
                attempts -= 1
                wrong_attempts += 1
                print(f"\033[34m{HANGMAN_ART[wrong_attempts]}\033[0m")
            else:
                print("That is correct!")
                blank = string_correction(guess, chosen_word, blank)
                print(f"You have {attempts} attempts left.")
            print(f"Current word: {blank}")
        else:
            attempts -= 1
            wrong_attempts += 1
            print(f"\033[34m{HANGMAN_ART[wrong_attempts]}\033[0m")
            print(f"Wrong guess. You have {attempts} attempts left.")
            print(f"Current word: {blank}")

    if "_" not in blank:
        return 1
    elif attempts == 0:
        return 2


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


def game_result(result, chosen_word):
    if result == 1:
        print("Congratulations, you've guessed the word!")
        print(f"\033[35m{Congrat_art}\033[0m")
    elif result == 2:
        print(f"Game over! The word was: {chosen_word}")
        print(f"\033[31m{Game_Over_art}\033[0m")
    elif result == 0:
        print("Something is wrong with the function hang_man()!")
    else:
        raise ValueError(f"Action not defined for result value {chosen_word}")

    return result


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    print("Welcome To Hang Man")
    print(f"\033[32m{Welcome_art}\033[0m")
    print("Start game hangman")
    result, chosen_word = hang_man()
    game_result(result, chosen_word)
    print(f"Game is done! Result value is: {result}")
