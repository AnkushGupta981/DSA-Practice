# Problem: Longest Substring Without Repeating Characters
# Platform: LeetCode
# Approach: Brute Force using Set
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        total = len(s)
        solution = 0
        for i in range(total):
            seen = set()
            for j in range(i, total):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    solution = max(solution, j - i + 1)
        return solution
