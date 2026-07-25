class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        nums.sort()
        n = len(nums)

        def dfs(index):
            # base case
            if index == n:
                dup = path.copy()
                dup.sort()
                if dup not in ans:
                    ans.append(dup)
                return 
            path.append(nums[index])

            dfs(index+1)

            path.pop()
            dfs(index+1)
        
        dfs(0)
        return ans