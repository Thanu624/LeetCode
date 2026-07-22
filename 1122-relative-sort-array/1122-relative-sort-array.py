class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for i in arr2:
            while i in arr1:
                result.append(i)
                arr1.remove(i)
        arr1.sort()
        return result + arr1