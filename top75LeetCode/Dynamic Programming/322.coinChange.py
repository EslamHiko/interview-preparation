'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''
'''
Compute the FEWEST number of coins than you need to make up that amount -> DP
Dp Template:

Goal: Compute the minimum number of coins to make up the amount

State : dp[i] the min num of coins to make up the amount i

BaseCase : dp[0] = the min num of 0 to make the amount 0

Recurrence :
    for coin in coins:
        dp[i] = min(dp[i],1+dp[i-coin])
Order of iteration :
    for i in range(amount + 1):
        for coin in coins:
            dp[i] = min(dp[i],1+dp[i-coin])

'''
def sol(coins,amount):
    dp = [float('inf') for _ in range(amount+1)]
    dp[0] = 0
    for i in range(amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i],1+dp[i-coin])
    return dp[amount] if dp[amount] != float('inf') else -1
