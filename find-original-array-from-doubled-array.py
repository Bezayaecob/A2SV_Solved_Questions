from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        changed.sort()
        countC = Counter(changed)
        original = []
        
        for x in changed:
            if countC[x] == 0:
                continue
            
            if countC[2*x] == 0:
                return []
            
            original.append(x)
            countC[x] -= 1
            countC[2*x] -= 1
        
        return original
