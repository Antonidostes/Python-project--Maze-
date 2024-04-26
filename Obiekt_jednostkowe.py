from Obiekt import Obiekt
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.ZK = "ZK"
        self.A = "A"

    def test_init(self):
        o1 = Obiekt(1, "ZK", 1)
        o2 = Obiekt(1, "A", 1)
        self.assertEqual(self.ZK, o1.type)
        self.assertEqual(self.A, o2.type)
        self.assertNotEqual(self.ZK, o2.type)


if __name__ == "__main__":
    unittest.main()