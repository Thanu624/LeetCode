class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length=len(nums)
        res=set()
        if length<4: return []
        nums.sort()
        for i in range(length-3):
            for j in range(i+1,length-2):
                a=j+1
                b=length-1
                while a<b:
                    curr=nums[i]+nums[j]+nums[a]+nums[b]
                    if curr==target:
                        res.add((nums[i],nums[j],nums[a],nums[b]))
                        a+=1
                        b-=1
                    elif curr>target:
                        b-=1
                    else:
                        a+=1
        return [list(x) for x in res]