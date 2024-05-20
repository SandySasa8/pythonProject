import unittest
from hangman1 import get_random_word, display_board, get_guess, play_hangman, display_hangman
import logging

logging.basicConfig(filename='test_log.log', level=logging.INFO)

class functia1(unittest.TestCase):

    def test_get_random_word(self):
        self.assertIn(get_random_word(), ['ciorba', 'scrisoare', 'animal', 'date', 'ananas'])
    """
    Verifica daca functia ia un cuvant din lista
    """
    def test_word_string(self):
        assert type(get_random_word()) is str
    """
    Verifica daca cuvantul returnat este un string
    """
    def test_correct_lenght(self):
        secret_word=get_random_word()
        assert len(secret_word) in range(4,10)
    """
    Verifica daca cuvantul secret este mai mic sau mai lung fata de 
    cel mai mic, respectriv cel mai lung cuvant din lista 
    """
    def setUp(self):
        self.original_get_random_word = get_random_word
        get_random_word.return_value = 'testword'
    """
    Verifica daca returneaza un cuvant pe care noi in impunem
    """

class functia2(unittest.TestCase):

    def test_display_board(self):
        missed_letters = 'abc'
        correct_letters = 'def'
        secret_word = 'mdneof'
        tries = 3
        display_board(missed_letters, correct_letters, secret_word,tries)
    """
    Verifica cum arata jocul
    """
class functia3(unittest.TestCase):
    def test_function(self):
        already_guessed = 'mno'
        get_guess(already_guessed)
    def test_get_guess(self):
        already_guessed = 'abc'
        guess = get_guess(already_guessed)
        self.assertNotIn(guess, already_guessed)
    """
    verifica ca litera introdusa de la tastatura sa fie una diferita 
    cu lista de litere deja incercate
    """

    def test_get_guess_valid_input(self):
        """
        Testeaza daca functia returneaza o singura litera
        """
        already_guessed = set()
        result = get_guess(already_guessed)
        self.assertEqual(len(result), 1)
class functia4(unittest.TestCase):
   
    def test_play_hangman(self):
        play_hangman()
    """
    Verifica daca jocul este jucat corect
    """
    def test_finish_message(self):
        missed_letters = 'abcd'
        self.assertEqual(len(missed_letters), 4)
    """
    Verifica daca mesajul de final, in cazul pierderii, va avea numarul corect de litere gresite
    """


class functi5(unittest.TestCase):
    def test_display_self(self):
        for i in range(7):
            self.assertIsInstance(display_hangman(i),str)
    "Verifica daca functia returneaza variabile de tip string "
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
        self.assertEqual(stages[1], """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """)
        """
        Verifica daca elementul cu indexul 1 din lista este cel asteptat
        """
if __name__ == '__main__':
    unittest.main()
    logging.info("Teste rulate cu succes!")