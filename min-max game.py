class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        def solve(n):
            if n==1:
                return 
            for i in range(n//2 ):
                if i %2==0:
                    nums[i]=  min(nums[2 * i], nums[2 * i + 1])
                else:
                    nums[i]=  max(nums[2 * i], nums[2 * i + 1])
            solve(n//2)
        solve(len(nums))
        return nums[0]
