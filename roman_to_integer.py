# Problem: Roman to Integer
# Platform: LeetCode
# Approach: Dictionary Mapping + Conditional Logic
# Time Complexity: O(n)
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        output = 0
        for i in range(len(s)):
            element= roman[s[i]]
            next_element= roman[s[i+1]] if i+1 < len(s) else 0

            if element < next_element:
                output-=element
            else:
                output+=element
        return output

