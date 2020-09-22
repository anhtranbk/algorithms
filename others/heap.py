import unittest


def heapify(arr: list[int]) -> list[int]:
    pass


class HeapTest(unittest.TestCase):
    def test_heapify(self):
        arr = [3,9,2,1,4,5]
        actual = heapify(arr)
        expected = [9,5,4,1,3,2]
        for i in range(len(arr)):
            self.assertEqual(arr)
    
    
if __name__ == "__main__":
    unittest.main()