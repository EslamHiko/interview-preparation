'''
The distance between 2 binary strings is the sum of their lengths after removing the common prefix. For example: the common prefix of 1011000 and 1011110 is 1011 so the distance is len("000") + len("110") = 3 + 3 = 6.

Given a list of binary strings, pick a pair that gives you maximum distance among all possible pair and return that distance.
'''
a=[i for i in input().strip().split()]
n=len(a)
maxDiff=float('-inf')
pair=[None,None]

for i in range(n):
    for j in range(i+1,n):
        l1,l2=len(a[i]),len(a[j])
        diff=0
        #breaked=False
        km=min(l1,l2)

        for k in range(min(l1,l2)):
            if a[i][k]!=a[j][k]:
                #diff=(l1-k)+(l2-k)
                #breaked=True
                km=k
                break
        diff=(l1-km)+(l2-km)
        if diff>maxDiff:
            pair=[a[i],a[j]]
            maxDiff=diff


print(pair)
print(maxDiff)
