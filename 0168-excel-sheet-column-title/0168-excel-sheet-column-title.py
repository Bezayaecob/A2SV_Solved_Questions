class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num=columnNumber
        res=""
        while num > 0:
            num-=1
            rem= num%26
            letter= chr(ord("A") +rem)
            res=letter + res
            num//=26
        return res 
            
        