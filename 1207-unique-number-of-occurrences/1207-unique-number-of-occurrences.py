class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurs = set()
        dic = {}
        for num in arr:
            if num in dic:
                dic[num] +=1
            else:
                dic[num] =1
        for num in dic:
            if dic[num] in occurs:
                return False
            else:
                occurs.add(dic[num])
        return True