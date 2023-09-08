import unittest

class HelloTestClass(unittest.TestCase):

    def test_hello(self):
        self.assertEqual('rubiks code'.upper(), 'RUBIKS COD')

if __name__ == '__main__':
    unittest.main()