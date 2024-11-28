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
            blank = string_correction(guess,chosen_word,blank)
            if "_" not in blank:
                result = 1
                break
            else:
                attemps -= 1
                print(f"Wrong guess. You have {attemps} attempts left.")
        if "_" not in blank:
            break
        elif attemps == 0:
            result = 0
            break
        
    return result, chosen_word
    
    
def string_correction(guess,chosen_word,blank):
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
    
    
def game_result(game_result, chosen_word) :
    res = 0
    if game_result == 1 :
        print("Congratulations, you've guessed the word!")
        res = 1
    elif game_result == 2 :
        print(f"Game over! The word was: {chosen_word}")
    elif game_result == 0:
        print(f"Something is wrong with the function hang_man()!")
    else: 
        raise ValueError(f"Action not defined for result value {chosen_word}")
    
    return res
   

if __name__ == '__main__':
    print("Start game hangman")
    res, chosen_word = hang_man()
    game_result(res, chosen_word)
    print(f"Game is done! Result value is: {res}")
    