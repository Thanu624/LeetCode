class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        path = []
        n = len(candidates)

        def dfs(index: int, remaining: int) -> None:

            if remaining == 0:
                ans.append(path.copy())
                return

            if remaining < 0 or index == n:
                return

            path.append(candidates[index])
            dfs(index, remaining - candidates[index])
            path.pop()

            dfs(index + 1, remaining)

        dfs(0, target)

        return ans