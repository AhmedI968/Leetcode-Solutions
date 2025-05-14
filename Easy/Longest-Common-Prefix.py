# LeetCode Longest Common Prefix
# My approach is to iterate through the characters of the first string and check if all other strings have the same character at that position.
# If they do, I add that character to the prefix. If any string does not match, I return the prefix found so far.
# The time complexity of this solution is O(n * m), where n is the number of strings and m is the length of the shortest string.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        prefix = ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return prefix
            
            prefix += char

        return prefix