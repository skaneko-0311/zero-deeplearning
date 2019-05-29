import unittest
import numpy as np
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

    def test_relu(self):
        self.assertEqual(af.relu(-1), 0)
        self.assertEqual(af.relu(0),  0)
        self.assertEqual(af.relu(1),  1)
        self.assertEqual(af.relu(5),  5)

    def test_identity_function(self):
        self.assertEqual(af.identity_function(-1), -1)
        self.assertEqual(af.identity_function(0),   0)
        self.assertEqual(af.identity_function(1),   1)
        self.assertEqual(af.identity_function(5),   5)

    def test_softmax(self):
        a = np.array([0.3, 2.9, 4.0])
        np.testing.assert_allclose(af.softmax(a),
                                   [0.01821127,
                                    0.24519181,
                                    0.73659691],
                                   rtol=1e-6, atol=0)


if __name__ == '__main__':
    unittest.main()
