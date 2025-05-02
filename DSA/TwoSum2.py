class Solution:
    def twosum2(self, nums:list[int], target:int)->list[int]:
        l=0
        r=len(nums)-1

        while l < r:
            if nums[l] + nums[r]<target:
                l+=1
            elif nums[l] + nums[r]>target:
                r-=1
            else:
                return [l+1, r+1]
        return


s=Solution()
print(s.twosum2(nums=[1, 2,3, 5, 7, 9, 13], target=20))