import unittest
import logic_circuit as lc


class TestMainMethods(unittest.TestCase):

    def test_AND(self):
        self.assertEqual(lc.AND(0, 0), 0)
        self.assertEqual(lc.AND(0, 1), 0)
        self.assertEqual(lc.AND(1, 0), 0)
        self.assertEqual(lc.AND(1, 1), 1)

    def test_NAND(self):
        self.assertEqual(lc.NAND(0, 0), 1)
        self.assertEqual(lc.NAND(0, 1), 1)
        self.assertEqual(lc.NAND(1, 0), 1)
        self.assertEqual(lc.NAND(1, 1), 0)

    def test_OR(self):
        self.assertEqual(lc.OR(0, 0), 0)
        self.assertEqual(lc.OR(0, 1), 1)
        self.assertEqual(lc.OR(1, 0), 1)
        self.assertEqual(lc.OR(1, 1), 1)

    def test_NOR(self):
        self.assertEqual(lc.NOR(0, 0), 1)
        self.assertEqual(lc.NOR(0, 1), 0)
        self.assertEqual(lc.NOR(1, 0), 0)
        self.assertEqual(lc.NOR(1, 1), 0)

    def test_XOR(self):
        self.assertEqual(lc.XOR(0, 0), 0)
        self.assertEqual(lc.XOR(0, 1), 1)
        self.assertEqual(lc.XOR(1, 0), 1)
        self.assertEqual(lc.XOR(1, 1), 0)

    def test_XAND(self):
        self.assertEqual(lc.XAND(0, 0), 1)
        self.assertEqual(lc.XAND(0, 1), 0)
        self.assertEqual(lc.XAND(1, 0), 0)
        self.assertEqual(lc.XAND(1, 1), 1)


if __name__ == '__main__':
    unittest.main()
