class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        cnts,pairs = [0]*(mx:= max(nums) +1), [0]*mx
        for num in nums:  cnts[num] += 1
        for ic in range(mx-1, 0, -1):
            pairs[ic] = (gs:= sum(cnts[ic::ic]))*(gs-1)//2 - sum(pairs[ic+ic::ic])
        pairs = [*accumulate(pairs)]
        return  [bisect_right(pairs, q) for q in queries]
        