class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]
        start = 0
        maxLength = 1

        # Every single char is a palindrome
        for i in range(n):
            dp[i][i] = True
        
        for length in range(2, n + 1): # Length of substring
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if length > maxLength:
                            start = i
                            maxLength = length
        
        return s[start:start + maxLength]