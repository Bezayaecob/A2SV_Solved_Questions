class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def checker(l,r):
            if l==r:
                return nums[l]
            tleft= nums[l]- checker(l+1,r)
            tright= nums[r]- checker(l, r-1) 
            return max(tleft, tright)

        return checker(0, len(nums) - 1) >= 0