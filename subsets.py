# Problem: Subsets
# Approach: Iterative subset expansion
# Time: O(n * 2^n)

class Solution:
    def subsets(self, nums):
        outer = [[]]
        for num in nums:
            n = len(outer)
            for i in range(n):
                outer.append(outer[i] + [num])
        return outer
