import unittest
import calc as cal


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = cal.add(10, 5)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
