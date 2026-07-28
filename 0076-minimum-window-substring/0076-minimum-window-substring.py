class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        hash_map = Counter(t)
        hash_map1 = Counter(t)
        i = [0, 0]
        minn = float('inf')
        for r in range(len(s)):
            if s[r] in hash_map and s[r] != 0:
                hash_map[s[r]] -= 1
            while max(hash_map.values()) == 0:
                if r - l + 1 < minn:
                    minn = r - l + 1
                    i = [l, r]
                if s[l] in hash_map and hash_map[s[l]] + 1 <= hash_map1[s[l]]:
                    hash_map[s[l]] += 1
                l += 1
        if minn == float('inf'):
            return ""
        else:
            return s[i[0] : i[1] + 1]