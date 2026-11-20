class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
       freq_nums=Counter(nums)
       return (sorted(freq_nums,key=freq_nums.get,reverse=True))[:k]