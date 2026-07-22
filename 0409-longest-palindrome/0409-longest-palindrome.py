class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        ans = 0
        for c in s:
            d[c] = d.get(c,0)+1
        for v in d.values():
            ans += (v//2)*2
        if ans<len(s):
            ans += 1
        return ans