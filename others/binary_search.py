import unittest

def test_binary_search(nums: list[int], k: int) -> int:
    if k < nums[0]:
        return 0 
    if k > nums[-1]:
        return len(nums)

    lo, hi = 0, len(nums)-1
    while lo < hi:
        m = lo + (hi-lo)//2
        if nums[m] < k:
            lo = m+1
        elif nums[m] > k:
            hi = m;
        else:
            return m
    return lo

    
class TestBinarySearch(unittest.TestCase):
    def test(self):
        self.assertEquals(test_binary_search([1,2,3,5,6,8,10], 1), 0)
        self.assertEquals(test_binary_search([1,2,3,5,6,8,10], 2), 1)
        self.assertEquals(test_binary_search([1,2,3,5,6,8,10], 3), 2)
        self.assertEquals(test_binary_search([1,2,3,5,6,8,10], 4), 3)
        self.assertEquals(test_binary_search([1,2,3,5,6,8,10], 5), 3)
        self.assertEquals(test_binary_search([1,2,3,5,6,8,10], 6), 4)
        self.assertEquals(test_binary_search([1,2,3,5,6,8,10], 7), 5)
        self.assertEquals(test_binary_search([1,2,3,5,6,8,10], 8), 5)
        self.assertEquals(test_binary_search([1,2,3,5,6,8,10], 9), 6)
        self.assertEquals(test_binary_search([1,2,3,5,6,8,10], 10), 6)

        self.assertEquals(test_binary_search([1,6], 0), 0)
        self.assertEquals(test_binary_search([1,6], 1), 0)
        self.assertEquals(test_binary_search([1,6], 2), 1)
        self.assertEquals(test_binary_search([1,6], 3), 1)
        self.assertEquals(test_binary_search([1,6], 6), 1)
        self.assertEquals(test_binary_search([1,6], 7), 2)


if __name__ == "__main__":
    unittest.main()