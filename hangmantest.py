import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'openai', 'computer']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |
           |
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |
           |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        '''
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6
    
    print("Welcome to Hangman!")
    
    while tries > 0 and word_letters:
        print(display_hangman(6 - tries))
        print("Word: ", ' '.join([letter if letter in guessed_letters else '_' for letter in word]))
        print(f"Tries left: {tries}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        if guess in word_letters:
            word_letters.remove(guess)
            guessed_letters.add(guess)
            print(f"Good job! '{guess}' is in the word.")
        else:
            tries -= 1
            guessed_letters.add(guess)
            print(f"Sorry, '{guess}' is not in the word.")
        print()
    
    if not word_letters:
        print(f"Congrats! You guessed the word '{word}' correctly!")
    else:
        print(display_hangman(6))
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()