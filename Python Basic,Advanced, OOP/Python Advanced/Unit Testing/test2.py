import unittest
import demo2

class TestMain(unittest.TestCase):

    def setUp(self):
        print("Testing a function")

    def test_input(self):
        # right guess
        answer = 5
        guess = 5
        result = demo2.run_guess(guess, answer)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        # wrong guess
        answer = 5
        guess = 0
        result = demo2.run_guess(guess, answer)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        # numbers only between 1-10
        answer = 5
        guess = 11
        result = demo2.run_guess(guess, answer)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        # what if input is string - return False from function
        answer = 5
        guess = '11'
        result = demo2.run_guess(guess, answer)
        self.assertIsInstance(result, ValueError)

    def tearDown(self):
        print("cleaning up")


if __name__ == '__main__':
    unittest.main()
