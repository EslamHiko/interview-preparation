'''
ref : https://leetcode.com/discuss/interview-question/396646/
input :
100
5
50 10 20 30 40
'''
maxToCollect = int(input())
n = int(input())
strawberries = [int(el) for el in input().split()]
res = 0

def dfs(strawberries,currIndex,collected,maxToCollect):
    if collected >= maxToCollect:
        return
    global res
    res = max(collected,res)
    for i in range(2,len(strawberries)):
        for j in range(currIndex,len(strawberries)):
            if i + j >= len(strawberries):
                break
            dfs(strawberries, i + j, collected+strawberries[i+j], maxToCollect)

for i in range(len(strawberries)):
    dfs(strawberries,i,strawberries[i],maxToCollect)


dp = {}
dp[0] = 0
dp[1] = strawberries[0]
for i in range(2,len(strawberries)+1):
    dp[i] = max(strawberries[i-1],strawberries[i-1]+dp[i-2])

f = [[0]*(maxToCollect+1)]*(len(strawberries)+1)
g = [[0]*(maxToCollect+1)]*(len(strawberries)+1)

for i in range(len(f)):
    f[i][0] = True
    g[i][0] = True

for i in range(1,len(f)):
    for j in range(1,len(f[0])):
        if j >= strawberries[i-1] and g[i-1][j - strawberries[i-1]]:
            f[i][j]=True
        g[i][j] = g[i-1][j] or f[i-1][j]


found = False
for i in range(len(f)):
    for j in range(len(f[0])):
        if f[len(f)-1-i][len(f[0])-1-j] or g[len(f)-1-i][len(f[0])-1-j]:
            print(len(f[0])-1-j)
            found = True
            break
    if found:
        break

print(dp[len(strawberries)])
print(res)
