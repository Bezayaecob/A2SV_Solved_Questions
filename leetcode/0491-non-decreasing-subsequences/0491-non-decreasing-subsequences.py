class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(start,path):

            if len(path) > 1:
                res.add(tuple(path[:]))
                # return
                
            for i in range(start,len(nums)):
                if not path:
                    path.append(nums[i])
                    backtrack(i+1,path)
                    path.pop()
                else:
                    if path[-1] <= nums[i]:
                        path.append(nums[i])
                        backtrack(i+1,path)
                        path.pop()

                        
        backtrack(0,[])
        return list(res)
                

                



        