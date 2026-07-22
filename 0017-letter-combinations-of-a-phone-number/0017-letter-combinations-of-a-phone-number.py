class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        p = {
            '2':'abc','3':'def','4':'ghi',
            '5':'jkl','6':'mno','7':'pqrs',
            '8':'tuv','9':'wxyz'
        }
        groups = [p[a] for a in digits]
        product = itertools.product(*groups)
        return ["".join(s) for s in product]