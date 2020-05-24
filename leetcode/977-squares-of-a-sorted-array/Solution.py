from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i, nums = 0, [0]*len(A)
        while i < len(A) and A[i] < 0:
            i += 1
        
        j, k = i-1, 0
        while i < len(A) and j >= 0:
            if abs(A[i]) <= abs(A[j]):
                nums[k] = A[i]*A[i]
                i += 1
            else:
                nums[k] = A[j]*A[j]
                j -= 1
            k += 1
        while i < len(A):
            nums[k] = A[i]*A[i]
            i, k = i+1, k+1
        while j >= 0:
            nums[k] = A[j]*A[j]
            j, k = j-1, k+1
        return nums
