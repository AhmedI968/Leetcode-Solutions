# Solution to the problem Regular Expression Matching on LeetCode.
# My approach is to use dynamic programming to solve the problem.
# The idea is to create a 2D table where dp[i][j] indicates whether the first i characters of the string s match the first j characters of the pattern p.
# The table is initialized with False values, and we set dp[0][0] to True because an empty string matches an empty pattern.
# We then iterate through the string and pattern, filling in the table based on the matching rules

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # This is a dp table
        # Intialize table
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # For empty string and empty pattern
        dp[0][0] = True

        for i in range(1, len(p) + 1):
            if p[i - 1] == "*":
                dp[0][i] = dp[0][i-2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i] [j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[len(s)][len(p)]