class Solution:
    def minOperations(self, nums: List[int]) -> int:
        oper = 0
        
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                oper += 1
                
                for j in range(i, i+3):
                    nums[j] = 1 - nums[j]
        
        if all(x == 1 for x in nums):
            return oper
        return -1