class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        from collections import Counter
           
        freq = Counter(nums)
        dominant = max(freq, key=freq.get)
        total = freq[dominant]
        
        leftCount = 0
    
        for i in range(len(nums) - 1):
            if nums[i] == dominant:
                leftCount += 1
            
            leftLength = i + 1
            rightLength = len(nums) - i - 1
            rightCount = total - leftCount
            
            if leftCount * 2 > leftLength and rightCount * 2 > rightLength:
                return i
        
        return -1

        
