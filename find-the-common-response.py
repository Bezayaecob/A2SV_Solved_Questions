from typing import List
from collections import Counter

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = Counter()
        
        for day in responses:
            for word in set(day):
                count[word] += 1
        
        if not count:
            return ""
        
        max_freq = max(count.values())
        common_response = [word for word, freq in count.items() if freq == max_freq]
        
        return min(common_response)
