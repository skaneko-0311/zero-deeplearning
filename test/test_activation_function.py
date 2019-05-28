import unittest
import activation_function as af


class TestActivationFunction(unittest.TestCase):

    def test_step_function(self):
        self.assertEqual(af.step_function(-1), 0)
        self.assertEqual(af.step_function(0),  0)
        self.assertEqual(af.step_function(1),  1)

    def test_sigmoid(self):
        self.assertEqual(af.sigmoid(-1), 0.2689414213699951)
        self.assertEqual(af.sigmoid(0),  0.5)
        self.assertEqual(af.sigmoid(1),  0.7310585786300049)


if __name__ == '__main__':
    unittest.main()
