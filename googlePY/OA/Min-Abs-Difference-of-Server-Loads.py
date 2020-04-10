'''
There are some processes that need to be executed. Amount of a load that process causes on a server that runs it, is being represented by a single integer. Total load caused on a server is the sum of the loads of all the processes that run on that server. You have at your disposal two servers, on which mentioned processes can be run. Your goal is to distribute given processes between those two servers in the way that, absolute difference of their loads will be minimized.

Given an array of n integers, of which represents loads caused by successive processes, return the minimum absolute difference of server loads.

Example 1:

Input: [1, 2, 3, 4, 5]
Output: 1
Explanation:
We can distribute the processes with loads [1, 2, 4] to the first server and [3, 5] to the second one,
so that their total loads will be 7 and 8, respectively, and the difference of their loads will be equal to 1.
'''
def sol(arr):
    minAbs = float('inf')
    calculated = {}
    def getRestArr(arr,load):
        tmp = list(arr)
        j = 0;
        i = 0
        while(i < len(tmp) and j < len(load)):
            if tmp[i] == load[j]:
                del tmp[i]
                j += 1
                continue
            i += 1

        return tmp
    for i in range(len(arr)):
        for j in range(i+1,len(arr)+1):
            load = (arr[i:j])
            rest = getRestArr(arr,load)

            loadSum = sum(load)
            restSum = sum(rest)
            if calculated.get((restSum,loadSum)) or calculated.get((loadSum,restSum)) and loadSum and restSum:
                continue

            minAbs = min(minAbs,abs(restSum-loadSum))
            calculated[(loadSum,restSum)] = 1
            calculated[(restSum,loadSum)] = 1

    return 0 if len(arr) == 0 else minAbs


print(sol([1,2,3,4,5]))
print(sol([10,10,9,9,2]))
print(sol([]))
print(sol([1]))

def sol2(arr):
    if not len(arr):
        return 0
    total = sum(arr)
    start = min(arr)
    dp = [False] * (total//2 + 1)
    dp[0] = True
    for s in arr:
        for i in range(total//2, start-1, -1):
            if s<=i and dp[i-s]:
                dp[i] = True
    # print(dp)
    for i in range(len(dp)-1, -1, -1):
        if dp[i]:
            return abs(2*i-total)

print('sol2')
print(sol2([1,2,3,4,5]))
print(sol2([10,10,9,9,2]))
print(sol2([]))
print(sol2([1]))
