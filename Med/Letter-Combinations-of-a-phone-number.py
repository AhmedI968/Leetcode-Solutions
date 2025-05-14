# LeetCode problem: Letter Combinations of a Phone Number
# My approach is to use a dictionary to map digits to their corresponding letters.
# I then use the itertools.product function to generate all possible combinations of letters for the given digits.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def generate_combninations(*strings):
            # Generate all possible combninations
            combination = list(itertools.product(*strings))

            # Convert the tuples to strings
            combninations = [''.join(comb) for comb in combination]

            return combninations

        dictNum = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        strings_pass = []

        if len(digits) == 0:
            return strings_pass

        for i in digits:
            strings_pass.append(dictNum[int(i)])

        combinations = generate_combninations(*strings_pass)
        return combinations