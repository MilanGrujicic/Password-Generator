import unittest
import utils

class TestCLIFunctions(unittest.TestCase):
    def test_generate_password(self):
       self.assertEqual(len(utils.generate_password(1, 1, 6)), 8)

if __name__ == '__main__':
  unittest.main()
