# Problem: Longest Common Prefix
# Platform: LeetCode
# Approach: Sorting + First and Last Comparison
# Time Complexity: O(n log n)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output=""
        strs=sorted(strs)
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))):
            if (first[i]!=last[i]):
                return output
            output+=first[i]
        return output

        
