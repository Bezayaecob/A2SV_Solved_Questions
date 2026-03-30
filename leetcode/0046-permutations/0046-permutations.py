class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    
            res=[]
            def dfs(current, remaining ):
                if len(current)==len(nums):
                    res.append(current[:])
                    return
                for num in remaining:
                    current.append(num)
                    dfs(current, [x for x in remaining if x!=num])
                    current.pop()
            dfs([],nums)
            return res 
        