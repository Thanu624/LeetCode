class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        start=-1
        end=-1
        output=[]
        i=0
        j=length-1
        while i<=j:
            if nums[i]==target:
                start=i
                break
            else:
                i+=1
        while i<=j:
            if nums[j]==target:
                end=j
                break
            else:
                j-=1
        output=[start,end]
        return output