import math
from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    l1, r1, l2, r2 = 0, len(nums1)-1, 0, len(nums2)-1
    mid = (len(nums1) + len(nums2)) // 2
    while True:
        m1 = (r1 - l1) // 2
        m2 = (r2 - l2) // 2
        if (m1-l1) + (m2-l2) > mid:
            if m1 > m2:
                r1 = m1
            else:
                r2 = m2
        else:
            pass


if __name__ == '__main__':
    nums1 = [1, 2, 3, 7, 8]
    nums2 = [1, 3, 4, 5, 6, 7, 9]
    ans = findMedianSortedArrays(nums1, nums2)
    print(ans)
