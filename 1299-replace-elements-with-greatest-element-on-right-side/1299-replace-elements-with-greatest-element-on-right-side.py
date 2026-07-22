class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr [i] = m
            if temp > m:
                m = temp
        return arr