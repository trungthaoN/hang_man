import random



print("Welcome To Hang Man")


def hang_man(): 
    result = 0 # something is wrong if return 0 
    
    vocab = ["Umbrella", "Laboratory", "Eccentric", "Dictionary", "Landscape",
            "Marathon", "Beautiful", "Volcanoes", "Adventure", "Quadratic"]
    start = input("Do you want to start the game Y/N ?").lower()
    attemps = 10
    while start == "y":
        chosen_word = vocab[random.randint(0, len(vocab)-1)].lower()
        blank = "_" * len(chosen_word)
        print(f"This word have {len(chosen_word)} characters: {blank}")
        while attemps > 0:
            guess = input("What is your guest (one word at a time only)?").lower()
            if len(guess) != 1:
                print("Please guess one letter at a time!")
                continue
            if guess in chosen_word:
                print("that correct")
                index = 0
                blank_space = ""
                while index < len(chosen_word):
                    if chosen_word[index] == guess:
                        blank_space += guess
                    else:
                        blank_space += blank[index]
                    index += 1
                blank = blank_space
                print(blank)
            if "_" not in blank:
                print("Congratulations, you've guessed the word!")
                result = 1
                break
            else:
                attemps -= 1
                print(f"Wrong guess. You have {attemps} attempts left.")
        if "_" not in blank:
            break
        elif attemps == 0:
            print(f"Game over! The word was: {chosen_word}")
            result = 0
            break
        
        return result 
    
    


if __name__ == '__main__':
    print("Start game hangman")
    res = hang_man()
    print(f"Game is done! Result value is: {res}")
    