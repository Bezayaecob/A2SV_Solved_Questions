class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        comp= dict()
        prefix= list(accumulate(nums))
        prefix=[0] + prefix
        for i, mod_val in enumerate(prefix):
            key = mod_val % k
            if key  in comp and i - comp[key] > 1:
                return True 
            elif key not in comp:
                comp[key] = i
        return False
