class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies)< k:
            return 0
        left =1
        right=max(candies)
        while left < right:
            mid= (left +right+1)//2
            total=sum(c//mid for c in candies )
            if total >= k:
                left = mid
            else:
                right = mid - 1
        
        return left