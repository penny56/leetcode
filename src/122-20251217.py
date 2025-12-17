from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        trendArr = []
        for i in range(len(prices)-1):
            trendArr.append(prices[i+1]-prices[i])
        
        # len of trendArr is one less than prices.
        profit = 0
        bought = False
        for i in range(len(prices)-1):
            if trendArr[i] > 0:
                # we buy
                if not bought:
                    priceIn = prices[i]
                    bought = True
            elif trendArr[i] < 0:
                # we sell
                if bought:
                    profit += prices[i]-priceIn
                    bought = False

        # in the last day, we sell it if we owned one
        if bought: profit += prices[-1]-priceIn

        return profit

if __name__ == "__main__":
    sol = Solution()
    res = sol.maxProfit([7,6,4,3,1])
    print(res)