#Given an integer array nums, return true if any value appears 
# at least twice in the array, and return false if every element is distinct.
class Solution:
    def ContainsDuplicate(self, nums:list[int])->bool:
        hashset=set() #we use set because it provides average O(1) time complexity  for both 
                      #insertion and membership check making it efficient for checking duplicates
        
        for n in nums:
          if n in hashset:
            return True
          hashset.add(n)
        return False


#@ Verification:
s=Solution()
#print(s.ContainsDuplicate(nums=[1, 2, 3]))
print(s.ContainsDuplicate(nums=[9, 8 ,4, 5 ,3, 4, 9]))