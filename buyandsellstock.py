class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """        
        maxprofit = 0

        if (len(prices) == 0):
            return 0
        
        left = 0
        right = left + 1
        
        while (right < len(prices)):
            
            diff = prices[right] - prices[left]
            
            if (diff <= 0):    
                left = right
                right += 1
            
            else:    
                profit = diff
                
                if (profit > maxprofit):
                    maxprofit = profit
                
                right += 1
        
        return maxprofit
        


print (Solution().maxProfit([7, 1, 2, 5, 3, 6, 4]))
