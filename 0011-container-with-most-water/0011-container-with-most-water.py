class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        m = 0

        while i < j:
            a = min(height[i], height[j]) * (j - i)
            if a > m:
                m = a

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return m