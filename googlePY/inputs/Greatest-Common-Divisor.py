'''
It said:
Failed level 3 test case
Input:
3
10
9 18
13 -1 8 8
12 26 -1 -1 6 9
Expected output:
7
Your output:
'''
def getGCD(a,b):
    if b == 0:
        return a
    return getGCD(b,a%b)

n = int(input())
minGCD = float('inf')
maxGCD = float('-inf')
for i in range(n+1):
    levels = {}
    levels[i] = []
    count = 0
    elements = input().split()
    for index in range(0,len(elements),2):
        if i != 0:
            levels[i].append([int(elements[index]),int(elements[index+1])])


    print(levels)
    if i != 0:
        for siblings in levels[i]:
            if siblings[0] == -1 or siblings[1] == -1:
                continue
            minGCD = min(minGCD,getGCD(siblings[0],siblings[1]))
            maxGCD = max(maxGCD,getGCD(siblings[0],siblings[1]))


print('Case #'+str(i+1)+': '+str(0 if minGCD == float('inf') else maxGCD - minGCD)+'\n')
