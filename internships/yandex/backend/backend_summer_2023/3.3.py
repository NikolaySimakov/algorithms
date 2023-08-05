from typing import List

def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0

    # initialize variables for first buy, first sell, second buy, and second sell
    buy1, buy2 = float('inf'), float('inf')
    sell1, sell2 = 0, 0

    d1 = d2 = d3 = d4 = 0
    
    for i in range(len(prices)):
        price = prices[i]
        
        if buy1 > price:
            buy1 = price
            d1 = i
            
        if sell1 < price - buy1:
            sell1 = price - buy1
            if i <= d3:
                d2 = i
        
        if buy2 > price - sell1:
            buy2 = price - sell1
            d3 = i
            
        if sell2 < price - buy2:
            sell2 = price - buy2
            d4 = i

    return d1+1, d2+1, d3+1, d4+1

prices = [1, 4, 2, 3, 3, 5]
print(maxProfit(prices))