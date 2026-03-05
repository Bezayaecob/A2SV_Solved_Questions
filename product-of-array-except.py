class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        run_mul=[]
        cur_mul=1
        for num in nums:
            run_mul.append(cur_mul)
            cur_mul*=num
        run_mul2=[]
        cur_mul2=1
        for i in range(len(nums) - 1, -1, -1):
            run_mul2.append(cur_mul2)
            cur_mul2*=nums[i]
        run_mul2.reverse()
        return [run_mul[i] * run_mul2[i] for i in range(len(nums))]
    

        
       
            
            

