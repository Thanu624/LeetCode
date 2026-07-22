class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [poured]
        for i in range(query_row):
            new =[0] * (i+2)
            for j in range(len(dp)):
                extra = max(0,(dp[j] - 1)/2)
                new[j] += extra
                new[j +1] += extra
            dp = new
        return min(1, dp[query_glass])
        