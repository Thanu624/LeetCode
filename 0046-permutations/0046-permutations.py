class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def f(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for num in nums:
                if num in curr:
                    continue

                curr.append(num)
                f(curr)
                curr.pop()

        f([])
        return res