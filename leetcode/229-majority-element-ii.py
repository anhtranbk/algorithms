from typing import List

class MedianSortedArrays:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ct1, ct2 = 0, 0
        cad1, cad2 = None, None
        for n in nums:
            if ct1 == 0:
                cad1 = n
            elif ct2 == 0:
                cad2 == n
            
            if count <= 0 and n not in ans:
                candidate = n
            count += (1 if n == candidate else -1)


if __name__ == '__main__':
    nums = [3,1,1,1,3,2,2,4]
    ret = MedianSortedArrays().majorityElement(nums)
    print(ret) 
