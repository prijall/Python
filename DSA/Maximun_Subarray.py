class Solution:
    def maxsubarrayval(self, nums:list[int])->int:
        maxval=nums[0]
        curVal=0

        for n in nums:
            if n < 0:
                curVal=0
            curVal += n
            maxval=max(maxval, curVal)
        return maxval


#@ What have i done here is that: 
# start from the beginning to end where ignore negative value
# if there is any positive value from there add it to current value
# current value is set to 0
# max value is set to first element in the list initially 
# find the max value between max value and current value
# return max value

