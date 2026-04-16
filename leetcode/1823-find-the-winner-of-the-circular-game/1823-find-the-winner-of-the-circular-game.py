class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def winner(a,b):
            if a==1:
                return 1
            return (winner(a-1,b) + b-1)% a +1
        return winner(n,k)
        