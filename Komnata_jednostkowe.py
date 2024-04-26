from Komnata import Komnata
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.numerA = 1
        self.numerB = 2

    def test_get_number(self):
        k = Komnata(1)
        self.assertEqual(self.numerA, k.get_number())
        self.assertNotEqual(self.numerB, k.get_number())
        with self.assertRaises(TypeError):
            k = Komnata("A")


if __name__ == "__main__":
    unittest.main()