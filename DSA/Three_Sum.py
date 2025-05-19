class Solution:
    def threesum(self, nums=list[int])->list[list[int]]:
        result=[]

        nums.sort()

        for i, n in enumerate(nums):  #this loop also helps to avoid duplication in solution
            if i > 0 and n==nums[i-1]:
                continue

            l, r=i+1, len(nums)-1 # initializes the pointer at the start of whole array, shifting of the pointer happens from while loop only
            
            while l < r:
                if n + nums[l] + nums[r] < 0:
                    l+=1
                elif n + nums[l] + nums[r] > 0:
                    r-=1
                else:
                    result.append([n, nums[l], nums[r]])

                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    
                    while l < r and nums[r] == nums[r -1]:
                      r -= 1

        return result
    
s=Solution()
print(s.threesum(nums=[-1,0,1,2,-1,-4]))

