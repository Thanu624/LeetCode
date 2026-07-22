class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1:
            total = 0
            while n > 0:
                digit =  n % 10
                total += digit * digit
                n = n // 10
            if total == 4:
                return False
            n = total
        return True