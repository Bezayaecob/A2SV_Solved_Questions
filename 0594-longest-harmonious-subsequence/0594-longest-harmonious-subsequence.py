from collections import Counter 
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        count= Counter(nums)
        res=0
        for n in count:
            if n+1 in count:
                res= max(res, count[n] +count[n+1])
        return res

        