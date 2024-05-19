import unittest
from hangman1 import get_random_word, display_board, get_guess, play_hangman, display_hangman

class functia1(unittest.TestCase):

    def test_get_random_word(self):
        self.assertIn(get_random_word(), ['ciorba', 'scrisoare', 'animal', 'date', 'ananas'])
    def test_word_string(self):
        assert type(get_random_word()) is str
    def test_correct_lenght(self):
        secret_word=get_random_word()
        assert len(secret_word) in range(4,10)
class functia2(unittest.TestCase):

    def test_display_board(self):
        missed_letters = 'abc'
        correct_letters = 'def'
        secret_word = 'abcdef'
        tries=1
        display_board(missed_letters, correct_letters, secret_word,tries)
        # Verify that the board is displayed correctly
class functia3(unittest.TestCase):

    def test_get_guess(self):
        already_guessed = 'abc'
        guess = get_guess(already_guessed)
        self.assertNotIn(guess, already_guessed)
    def test_function(self):
        already_guessed="ad"
        get_guess(already_guessed)
class functia4(unittest.TestCase):

    def test_play_hangman(self):
        play_hangman()
        # Verify that the game is played correctly
class functi5(unittest.TestCase):
    def test_display_self(self):
        for i in range(7):
            self.assertIsInstance(display_hangman(i),str)
    def test_disply_pozitia_0(self):
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
                """]
        self.assertEqual(stages[1],"""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """)
if __name__ == '__main__':
    unittest.main()