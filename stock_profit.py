'''

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve. If you cannot achieve any profit, return 0.
Examples:
pythonExample 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.


'''



from math import inf

def max_profit(arr):

    min_val  = float(inf)

    max_profit=0

    for price in arr:

        min_val = min(min_val,price)  ##store the minium value

        profit = price - min_val  ##calculatre the profit if we sell today

        max_profit = max(max_profit,profit)  ##get the maximum profit vlaue

    return max_profit

val=[7,1,5,3,6,4]
print(max_profit(val))


