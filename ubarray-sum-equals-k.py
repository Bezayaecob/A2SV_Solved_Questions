
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
              
        comp= defaultdict(int)
        comp[0]=1
        curr_sum=0

        count=0
        for num in nums:
            curr_sum+=num
            diff=curr_sum-k
            if diff in comp:
                count+=comp[diff]
            comp[curr_sum]+=1
        return count 
    
            
        
        


    
        
                   
