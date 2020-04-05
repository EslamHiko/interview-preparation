

'''
Remove Duplicates from array
'''
def removeDuplicates(arr):
    existsMap = {}
    finalMap = []
    for i in arr :
        ##if i not in existsMap:
        if not existsMap.get(i) :
            finalMap.append(i)
        existsMap[i] = 1
    return finalMap

print(removeDuplicates([1,2,2,3,4]))

## must be in order
def checkStrSub(str1,str2):
    if len(str2) > len(str1) :
        str1,str2 = str2,str1
    j = 0;

    for i in range(len(str1)):

        if (str2[j] if j < len(str2) else None) == str1[i] :
            j += 1

    return j == len(str1) or j == len(str2)

print(checkStrSub("ade","fefaefdeffef"))
print(checkStrSub("zxx","fefefeffefda"))

## can be not in order
def checkStrSubNoOrder(str1,str2):
    if len(str2) > len(str1) :
        str1,str2 = str2,str1
    j = 0;
    hashMap = {}
    for el in str2 :
        if(hashMap.get(el)):
            hashMap[el] += 1;
        else :
            hashMap[el] = 1;
    print(hashMap)


    for i in range(len(str1)):
        if hashMap.get(str1[i]):
            j += 1
            hashMap[str1[i]] -= 1

    return j == len(str1) or j == len(str2)

print(checkStrSubNoOrder("ade","fefefdeffaef"))
print(checkStrSubNoOrder("adae","fefefdeffaef"))
print(checkStrSubNoOrder("adae","fefaefdeffaef"))
print(checkStrSubNoOrder("zxx","fefefeffefda"))

def checkForSum(arr,sum):
    sol = []
    needed = {}
    for el in arr:
        if(needed.get(el)):
            sol.append((el,needed.get(el)))
        needed[sum-el] = el;

print(checkForSum([1,2,4,4,6],8))

'''
For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

'''
def getHowManyLessInTheRight(arr):
    result = []
    for i in range(len(arr)):
        sum = 0
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                sum += 1
        result.append(sum)
    return result

print(getHowManyLessInTheRight([3, 4, 9, 6, 1]))


def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    def checkCell(states2,i):
        if(i == 0):
            return states2[1] == 0
        if(i == len(states2)-1):
            return states2[len(states2)-2] == 0

        cond1 = states2[i+1] and states2[i-1];
        cond2 = not states2[i+1] and not states2[i-1]

        return cond1 or cond2

    for d in range(days):
        temp = states.copy()
        for state in range(len(states)):
            if(checkCell(states,state)):
                temp[state] = 0
            else:
                temp[state] = 1
        states = temp
    return states

def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    def gcd(x,y):
        while(y):
            x, y = y, x % y
        return x
    curr = arr[0]
    for el in range(1,len(arr)) :
        curr = gcd(curr,arr[el])
    return curr

from itertools import permutations, combinations


features = ['A', 'B', 'C']
tmp = []
for i in range(len(features)):
    oc = combinations(features, i + 1)
    for c in oc:
        tmp.append(list(c))
print(tmp)
print("abcdef".find("zs"))
def suggestedProducts(products, searchWord):
        finalArr = []
        for i in range(len(searchWord)):
            newArr = []
            for product in products:
                if product.find(searchWord[0:i]) != -1:
                    newArr.append(product)
            finalArr.append(newArr)
        return finalArr
print(suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"],"mouse"))
print(suggestedProducts(["havana"],"havana"))

def searchMatrix(m, v):
        for i in m:
            for j in i:
                if j == v:
                    return True
        return False
print(searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],5))
print(searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],20))

23280704933245
23280727206101
