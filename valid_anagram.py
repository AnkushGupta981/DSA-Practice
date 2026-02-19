# Problem: Valid Anagram
# Approach: Sorting comparison
# Time: O(n log n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
