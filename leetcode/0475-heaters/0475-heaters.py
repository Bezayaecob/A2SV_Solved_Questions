from bisect import bisect_left
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res=0
        for house in houses:
            index= bisect_left(heaters,house)
            right = abs(heaters[index] - house) if index < len(heaters) else float('inf')
            left = abs(heaters[index-1] - house) if index > 0 else float('inf')
            
            closest= min(left,right)
            res = max(res,closest)
        return res
        

        