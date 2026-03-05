class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
       
        comp= defaultdict(int)
        comp[0]=1
        curr_sum=0

        count=0
        for num in nums:
            curr_sum+=num
            diff=curr_sum-goal
            if diff in comp:
                count+=comp[diff]
            comp[curr_sum]+=1
        return count 
    

                


        
