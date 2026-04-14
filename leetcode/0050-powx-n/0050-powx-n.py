class Solution:
    def myPow(self, x: float, n: int) -> float:
           
        def pow(b,e):
            if e == 1:
                return b
            if e == 0:
                return 1
            
            val = pow(b, e // 2)
            res = val * val
            if e % 2 == 0:
                return val * val
            else:
                return val * val * b
        
        if n < 0:
            val = pow(x, n * -1)
            return 1 / val
        return pow(x, n)