class Solution:
    def threeSum(self, nums):
        visited = set()
        rs = set()
        for i in range(0, len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])

            d = dict()
            x = nums[i]
            for j in range(i+1, len(nums)):
                if i != j:
                    d[-x-nums[j]] = j
                    
            for j in range(i+1, len(nums)):
                y = nums[j]
                if y not in d or d[y] == j:
                    continue
                z = -(x + y)
                low = min(x, min(y, z))
                high = max(x, max(y, z))
                # print(low, -(low+high), high)
                rs.add((low, -(low+high), high))
        return rs
