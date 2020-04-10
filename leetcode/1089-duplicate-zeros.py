class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l, r = 0, len(arr)-1
        while l < r:
            if arr[l] == 0:
                r -= 1
            l += 1
        i, j = r, len(arr)-1
        while i >= 0 and j > i:
            if arr[i] != 0:
                arr[j] = arr[i]
                j -= 1
            else:
                arr[j] = 0
                arr[j-1] = 0
                j -= 2
            i -= 1
