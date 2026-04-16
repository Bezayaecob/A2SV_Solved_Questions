class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        count= Counter(nums)
        for i in range( 1, len(nums)+1):
            if count[i]>1:
                return i
                
        