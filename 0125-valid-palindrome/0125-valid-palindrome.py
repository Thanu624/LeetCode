class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = [i.lower() for i in s if i.isalnum()]
        return a == a[::-1]        