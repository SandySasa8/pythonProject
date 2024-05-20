import random


words = ['ciorba', 'scrisoare', 'animal', 'date', 'ananas']

def get_random_word():
    return random.choice(words)
    """
    Returneaza un cuvant aleatoriu din lista words
    """

def display_board(missed_letters, correct_letters, secret_word, tries):
    """
    Ce apare in timpul jocului
    """
    print()
    print(display_hangman(tries))
    for letter in secret_word:
        if letter in correct_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')

def get_guess(already_guessed):
    """
    Pentru a introduce litera si pentru afisarea mesajlor cu referire la litera introdusa
    """
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        else:
            return guess

def play_hangman():
    """
    Arata ce litere au fost folosite, literele corecte le arata unde sunt in cuvant si
    afiseaza mesajele pentru finalul jocului
    """
    tries = 6
    secret_word = get_random_word()
    correct_letters = ''
    missed_letters = ''

    while True:
        display_board(missed_letters, correct_letters, secret_word, tries)
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters += guess

            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break

            if found_all_letters:
                print('Yes! The secret word is "' + secret_word + '"! You have won!')
                break
        else:
            missed_letters += guess
            tries -= 1
            if tries == 0:
                display_board(missed_letters, correct_letters, secret_word, tries)
                print('You have run out of guesses!\nAfter ' + str(len(missed_letters)) + ' missed guesses and ' + str(len(correct_letters)) + ' correct guesses, the word was "' + secret_word + '"')
                break


def display_hangman(tries):
    """Desenul pentru spanzuratoare"""
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]