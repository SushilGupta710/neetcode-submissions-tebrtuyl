class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #neet code solution
        #Solve with two pointer assing l as 0 and r as 1
        #as first and second element
        l,r=0,1
        maxProfit=0
        #run the loop till last element of array
        while r < len(prices):
            #check if price[l] is less then price of r then check the profit via 
            #substrating and put it in max profit
            if(prices[l] < prices[r]):
                profit = prices[r] - prices[l]
                maxProfit=max(maxProfit,profit)
            else:
                #assign l to r because we know r value is smaller so l value got updated
                l = r
            r+=1 # increase right side to tract right value 
        return maxProfit

