import unittest


class TestGame(unittest.TestCase):
    """
    (solutions/beginning)
    There should only be one failing test to show general structure of test
    For help - see https://docs.python.org/2.7/library/unittest.html#module-unittest
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_that_fails(self):
        """This test should fail"""
        self.assertEqual("fia med knuff", "gomoku", msg="names must be equal")


if __name__ == '__main__':
    unittest.main()
