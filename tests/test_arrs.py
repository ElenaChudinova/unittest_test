import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([-1, -2, -3], 1, "test"), -2)
        self.assertEqual(arrs.get(['a', 'b', 'c'], 2, "test"), 'c')
        self.assertEqual(arrs.get([50.5, 55.1, 60.3], 1, "test"), 55.1)



    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([], 0), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], None), [])

