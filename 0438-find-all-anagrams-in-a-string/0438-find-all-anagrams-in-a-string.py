class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        c = Counter(p)
        result = []
        for i in range(len(s)-len(p) +1):
            temp = Counter(s[i:i+len(p)])
            if temp == c:
                result.append(i)
        return result