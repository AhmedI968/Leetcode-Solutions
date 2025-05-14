# LeetCode Problem: Integer to Roman
# My approach is to use a greedy algorithm to convert an integer to a Roman numeral.
# The idea is to start with the largest Roman numeral value and subtract it from the integer until the integer becomes zero.
# I maintain a list of values and their corresponding Roman symbols.
# I iterate through the list of values and for each value, I check if the integer is greater than or equal to that value.
# If it is, I append the corresponding Roman symbol to the result string and subtract the value from the integer.
# I repeat this process until the integer becomes zero.
# Could have been more efficient by using a dictionary instead of two lists.

class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        res = ""
        for i in range(len(val)):
            while num >= val[i]:
                res += symbols[i]
                num -= val[i]
        
        return res