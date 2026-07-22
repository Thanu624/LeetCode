class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(a):
            return a == a[::-1]
        i,j = 0,len(s) -1
        while i<j:
            if s[i] != s[j]:
                return check(s[i+1:j+1]) or check(s[i:j])
            i += 1
            j -= 1
        return True