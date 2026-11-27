class Solution:
    def reversePrefix(self, s: str, k: int) -> str:

        return ''.join([s[k - 1::-1],s[k:]])
        