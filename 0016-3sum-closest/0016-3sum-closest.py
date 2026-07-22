class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min1=sum(nums[:3])

        for i in range(len(nums)-2): #it will consider 3 elements. exapmle for len=6 idxs=0,1,2,3,4,5  we need till 3 so that 3,4,5 will be the last combination after that if will be less than 3
            left=i+1
            right=len(nums)-1
            while left<right:
                curr_sum=nums[i]+nums[left]+nums[right]
                if abs(target-curr_sum)<abs(target-min1):
                    min1=curr_sum
                if curr_sum<target:
                    left+=1
                elif curr_sum>target:
                    right-=1
                else:
                    return target
        return min1
