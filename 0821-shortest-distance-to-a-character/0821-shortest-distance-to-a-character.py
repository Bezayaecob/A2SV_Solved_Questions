class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        pos=[]
        for i in range(len(s)):
            if s[i]== c:
                pos.append(i)
        res=[]
        for i in range(len(s)):
            distance=[]
            for num in pos:
                distance.append(abs(i-num))
            res.append(min(distance))
        return res

        