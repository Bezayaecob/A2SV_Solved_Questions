class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num=columnTitle
        res=0
        for letter in num:
            val= ord(letter)-ord("A")+1
            res= res*26 +val
        return res
