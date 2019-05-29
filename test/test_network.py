import unittest
import numpy as np
import network as nw


class TestNetwork(unittest.TestCase):

    def test_init_network(self):
        network = nw.init_network()
        np.testing.assert_array_equal(network['W1'],
                                      np.array([[0.1, 0.3, 0.5],
                                                [0.2, 0.4, 0.6]]))

        np.testing.assert_array_equal(network['b1'],
                                      np.array([0.1, 0.2, 0.3]))

        np.testing.assert_array_equal(network['W2'],
                                      np.array([[0.1, 0.4],
                                                [0.2, 0.5],
                                                [0.3, 0.6]]))

        np.testing.assert_array_equal(network['b2'],
                                      np.array([0.1, 0.2]))

        np.testing.assert_array_equal(network['W3'],
                                      np.array([[0.1, 0.3],
                                                [0.2, 0.4]]))

        np.testing.assert_array_equal(network['b3'],
                                      np.array([0.1, 0.2]))

    def test_forward(self):
        network = nw.init_network()
        x = np.array([1.0, 0.5])
        y = nw.forward(network, x)
        self.assertEqual(y[0], 0.3168270764110298)
        self.assertEqual(y[1], 0.6962790898619668)


if __name__ == '__main__':
    unittest.main()
