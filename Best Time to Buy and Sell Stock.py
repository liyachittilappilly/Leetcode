class Solution(object):
    def maxProfit(self, prices):
        minprice=float('inf')
        maxprofit=0
        for p in prices:
            if p<minprice:
                minprice=p
            profit=p-minprice
            if profit>maxprofit:
                maxprofit=profit
        return maxprofit
