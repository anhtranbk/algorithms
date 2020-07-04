from sys import exc_info
import unittest
from typing import List, Any

class BaseTestCase(unittest.TestCase):
    def assertArrayEquals(self, 
        expected: List[Any], 
        actual: List[Any], 
        sorted_before_comparing=False, 
        exec_info=True
    ):
        self.assertEqual(len(expected), len(actual))

        if sorted_before_comparing:
            expected = sorted(expected)
            actual = sorted(actual)

        for i in range(0, len(expected)):
            try:
                self.assertEqual(expected[i], actual[i])
            except Exception:
                if exc_info:
                    print('Exception when asserting at element ' + str(i))
                    print('Expected', expected)
                    print('Actual', actual)
                raise
