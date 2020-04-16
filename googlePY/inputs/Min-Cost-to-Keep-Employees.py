'''
ref : https://leetcode.com/discuss/interview-question/397339/
'''
def solver(cost,salary,severance,nums):
    dp = {0:0}
    for req in nums:
        tmp = collections.defaultdict(lambda: float('inf'))
        for key in dp:
            # if employees are more than required
            if key >= req:
                for i in range(req,key+1):
                    # tmp[i] currMin,
                    # dp[key] is salary Min sum +
                    # i*salary is all over salaries
                    # (key-i)*severance tyring to let key-i employees go
                    tmp[i] = min(tmp[i],dp[key]+i*salary+(key-i)*severance)
            else:
                tmp[req] = min(tmp[req],dp[key]+req*salary+(req-key)*cost)
        dp = tmp
    return min(dp.values())
