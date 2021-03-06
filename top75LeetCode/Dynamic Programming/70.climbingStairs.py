'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
# memorization / recursion
def sol1(n):
    def climbStairs(i,n,memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo.get(i):
            return memo[i]

        memo[i] = climbStairs(i+1,n,memo) + climbStairs(i+2,n,memo)

        return memo[i]

    memo = {}
    return climbStairs(0,n,memo)
# DB approach
def sol2(n):
    if n == 1:
        return 1
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[n]

print(sol1(6))   # 13
print(sol2(6))   # 13
