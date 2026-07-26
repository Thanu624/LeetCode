class Solution:
    def maximumProduct(self, a: List[int]) -> int:
        return max(prod((q:=sorted(a))[-3:]),q[0]*q[1]*q[-1])