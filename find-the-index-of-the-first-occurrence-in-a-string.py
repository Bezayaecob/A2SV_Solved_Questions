class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1 
        start=0
        end=len(needle) 
        while end <= len(haystack):
            if needle== haystack[start:end]:
                    return start
            end+=1
            start+=1
        return -1

        
             
