class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        dp = {(0, 0): 1}
        for num in nums:
            ndp = dp.copy()
            for (i, j), count in dp.items():
                gi = gcd(i, num)
                if i == j:
                    ndp[(gi, j)] = (ndp.get((gi, j), 0) + 2 * count) % MOD
                else:
                    ndp[(gi, j)] = (ndp.get((gi, j), 0) + count) % MOD
                    gj = gcd(j, num)
                    key = (i, gj) if i <= gj else (gj, i)
                    ndp[key] = (ndp.get(key, 0) + count) % MOD

            dp = ndp

        ans = 0
        for i in range(1, max(nums) + 1):
            ans = (ans + dp.get((i, i), 0)) % MOD

        return ans