import unittest
import leap

class TestCase(unittest.TestCase):
    def test_leap1(self):
        self.assertEqual(leap.leap(2000), True)
    def test_leap2(self):
        self.assertEqual(leap.leap(2011), False)
    def test_leap3(self):
        self.assertEqual(leap.leap(2100), False)


if __name__ == '__main__':
    unittest.main()