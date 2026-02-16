from collections import defaultdict

class Solution:
    def findValidPair(self, s: str) -> str:
        result = defaultdict(int)
            
        for digit in s:
            result[digit] += 1
               
        for i in range(len(s) - 1):
            a = s[i]
            b = s[i + 1]
            
            if a != b and result[a] == int(a) and result[b] == int(b):
                return a + b
        
        return ""

