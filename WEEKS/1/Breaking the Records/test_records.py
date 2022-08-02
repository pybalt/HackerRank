import unittest
import records
import pytest


class ReturnFunction(unittest.TestCase):

    def test_return(self):
        self.assertEqual(records.breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]), [2, 4])
        self.assertEqual(records.breakingRecords([1, 10, 30, 10, 35]), [3, 0])
        self.assertEqual(records.breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]), [4, 0])
        self.assertEqual(records.breakingRecords([6, 10, 10, 5, 3]), [1, 2])
        self.assertEqual(records.breakingRecords([55, 40, 30, 25, 75]), [1, 3])
        self.assertEqual(records.breakingRecords([2, 3, 5, 10, 35, 1]), [4, 1])
        self.assertEqual(records.breakingRecords([1, 1, 1, 103, 35]), [1, 0])
        self.assertEqual(records.breakingRecords([1, 80, 24]), [1, 0])