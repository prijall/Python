
import math
class Solution:
    def koko(self, piles:list[int], h:int)->int:
        l, r=1, max(piles)
        res=r
        
        
        while l<=r:  
            k=l+ (r-l)//2
            total_time=0
            for p in piles:
                total_time+=math.ceil(p/k)

            if total_time <= h:
                    res=k
                    r=k-1
            else:
                    l=k+1
        return res


s=Solution()
print(s.koko(piles = [25,10,23,4], h = 4))
