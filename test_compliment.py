import unittest

from spaceman import is_word_guessed
from spaceman import get_guessed_word
from spaceman import is_guess_in_word


class GetCompliment(unittest.TestCase):
    # For each test in the class, make a method where self is the parameter
    # compliments = ['coolio', 'smashing', 'neato', 'fantabulous']

    def test_is_word_guessed(self):

        assert is_word_guessed('fish','fish') is True
        assert is_word_guessed('NO', 'Yes') is False

    def test_get_guessed_word(self):

        assert get_guessed_word('Dragon','Dragon') == 'Dragon'
        assert get_guessed_word('Griphon','Sphyinx') == '_ _ iph_ n'


    def test_is_guess_in_word(self):

        assert is_guess_in_word('a','Rathalos') == True
        assert is_guess_in_word('X','Teostra') == False



    # def test_get_compliment(self):
    #     # the actual test
    #     self.assertEqual(get_compliment(),f'Hello there, user! You are so {compliments[0]}!')

# run the tests
if __name__ == '__main__':
    unittest.main()
