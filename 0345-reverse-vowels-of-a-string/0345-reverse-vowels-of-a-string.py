class Solution:
    def reverseVowels(self, s: str) -> str:
        v="aeiouAEIOU"
        a=[c for c in s if c in v]
        r=""
        for c in s:
            if c in v:
                r += a.pop()
            else:
                r += c
        return r