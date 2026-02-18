class Solution:
    def minSteps(self, s: str, t: str) -> int:
               
        countS = Counter(s)
        countT = Counter(t)        
        steps = 0      
        for ch in countS:
            if countS[ch] > countT[ch]:
                steps += countS[ch] - countT[ch]
        
        return steps
