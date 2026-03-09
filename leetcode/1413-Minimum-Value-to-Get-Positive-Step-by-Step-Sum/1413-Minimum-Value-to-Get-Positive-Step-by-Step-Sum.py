class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        min_prefix=0
        prefix=0
        for num in nums:
            prefix+=num
            min_prefix=min(min_prefix,prefix)
        return 1- min_prefix