class Solution:
    def hammingWeight(self, n: int) -> int:
     
        res = []

        def bits(n):
            if n == 0:
                return

            res.append(n % 2)
            bits(n // 2)

        bits(n)

        count = sum(res)

        return count
      
