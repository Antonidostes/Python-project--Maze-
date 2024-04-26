from Gra import Gra
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.numerA = 1
        self.numerB = 2

    def test_convertable_to_int(self):
        p1 = Gra.convertable_to_int(self, "1")
        p2 = Gra.convertable_to_int(self, "a")
        self.assertEqual(True, p1)
        self.assertNotEqual(True, p2)

    def test_convertable_to_float(self):
        p1 = Gra.convertable_to_float(self, "2.3")
        p2 = Gra.convertable_to_float(self, "a")
        self.assertEqual(True, p1)
        self.assertNotEqual(True, p2)

    def test_required(self):
        p1 = Gra.required(self, 15)
        p2 = Gra.required(self, 17)
        self.assertEqual(True, p1)
        self.assertEqual(True, p2)

    def test_required_real(self):
        p1 = Gra.required_real(self, 0.3, 0.2, 0.4)
        p2 = Gra.required_real(self, 0.5, 0.2, 0.4)
        self.assertEqual(True, p1)
        self.assertNotEqual(True, p2)

if __name__ == "__main__":
    unittest.main()
