class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #chat gpt
        minPrice = float('inf')
        maxProfit=0
        for price in prices:
            if price < minPrice:
                minPrice=price
            #calcular the profit
            profit = price - minPrice
            maxProfit = max(maxProfit,profit)
        return maxProfit
