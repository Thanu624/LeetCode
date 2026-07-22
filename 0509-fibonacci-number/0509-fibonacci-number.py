class Solution:
    def fib(self, n):

        ft, st = 0, 1

        for _ in range(1, n + 1):
            tt = ft + st
            ft = st
            st = tt

        return ft