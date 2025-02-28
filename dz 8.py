import unittest

def multiply(a, b):
    return a * b

class TestMultiply(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply(2, 3), 6)

if __name__ == '__main__':
    unittest.main()
