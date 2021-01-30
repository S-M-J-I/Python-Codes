
import unittest

# import the file u want to test or the function from file
import demo1


class TestMain(unittest.TestCase):

    # We are doing multiple tests on a certain function, by changing parameters and
    # matching the change with the expected (or returned) values

    def setUp(self):
        # allows us to run a piece of code that sets up before each call of tests
        print("Testing a function") 

    def test_do_stuff(self):
        test_param = 10
        result = demo1.do_stuff(test_param)
        self.assertEqual(result, 15)  # (getvalue,expected value)
        # make sure the parameters are equal (ie 10+5 = 15)

    def test_do_stuff2(self):
        test_param = 'shkskhss'
        result = demo1.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))  # to check if something is true
        # or self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = demo1.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = demo1.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def tearDown(self):
        # run at the end of each test called
        print("cleaning up")  # used for resetting variables, etc


if __name__ == '__main__':
    unittest.main()  # will run the entire test file within TestMain class



# if successful = Tests run. OK
# if failure, it will be mention in which line and how to fix the code
# the test file fails (not the main program)

# go to unit test documentation. **IMP**


# usually we have more than one file at a time and each function is tested with a different module
# python3 -m unittest

# now if we create another file that has another set of tests. Both test files
# will run together

# python3 -m unittest -v = -v gives more information on the tests

