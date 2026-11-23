
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [0] * (k + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            new_dp = [0] * (k + 1)

            for j in range(k + 1):
                new_dp[j] = dp[j]

                if j > 0:
                    new_dp[j] += new_dp[j - 1]

                if j >= i:
                    new_dp[j] -= dp[j - i]

                new_dp[j] %= MOD

            dp = new_dp

        return dp[k]
