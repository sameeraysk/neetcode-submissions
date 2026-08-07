class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit=0
        for i  in range(n):
            for j in range(i+1,n):
                if prices[i]<prices[j]:
                    prof_val=prices[j]-prices[i]
                    profit=max(profit,prof_val)
                
        return profit