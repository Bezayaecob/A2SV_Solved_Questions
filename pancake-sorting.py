class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n= len(arr)
        res=[]
        lst= arr[:]
        def flip(k):
            nonlocal lst
            f = lst[:k]
            last= lst[k:]
            f=f[::-1]
            f.extend(last)
            lst=f[:]
            return 
        for size in range(n,0,-1):
            max_index= lst.index(size)
            if max_index==size-1:
                continue 
            if max_index!=0:
                res.append(max_index+1)
                flip(max_index+1)
            res.append(size)
            flip(size)
        return res 

            
                


        
