class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
       
        piles.sort(reverse=True)
        
        max_coins = 0
        n = len(piles) // 3
        
        for i in range(n):
            
            max_coins += piles[2 * i + 1]
        
        return max_coins



        
