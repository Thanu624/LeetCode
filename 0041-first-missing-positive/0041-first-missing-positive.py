class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums) + 1
        nums = set(nums)


        for num in range(1, l):
            if num not in nums:
                return num
        

        return l