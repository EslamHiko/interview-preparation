#
# Complete the 'minimumOperations' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY numbers as parameter.
#
import collections
def minimumOperations(numbers):
    # Write your code here
    '''
    count = 1
    newArr = collections.deque()
    newArr.append(numbers[0])
    currMaxIndex = 0
    currMax = numbers[0]
    currMaxMap = {numbers[0]:0}
    for i in range(1,len(numbers)):
        j = currMaxMap[currMax] if numbers[i] > currMax else 0
        while j <= len(newArr) and j >= 0:
            if j == len(newArr):
                newArr.append(numbers[i])
                currMax = numbers[i]
                currMaxMap[numbers[i]] = j
                count += 1
                break
            cond = numbers[i] > newArr[j]
            if j >= len(newArr)/2:
                cond = numbers[i] >= newArr[j]
            if cond:
                j += 1
            else:
                if j == 0:
                    newArr.appendleft(numbers[i])
                    count += 1
                    break
                else:
                    newArr.insert(j,numbers[i])
                    count += min(j*2+1,(len(newArr)-1-j)*2+1)
                    break
    return count
    '''
    def findPos(arr,target):
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if (arr[mid] > target):
                high = mid
            else:
                low = mid + 1
        return low;
    count = 1
    newArr = collections.deque()
    newArr.append(numbers[0])
    for i in range(1,len(numbers)):
        if numbers[i] <= newArr[0]:
            count += 1
            newArr.insert(0,numbers[i])
            continue
        if numbers[i] >= newArr[-1]:
            count += 1
            newArr.append(numbers[i])
            continue

        p = findPos(newArr,numbers[i])
        newArr.insert(p,numbers[i])
        k = p
        l = p
        if newArr[k] == newArr[k-1]:
            while newArr[k] == newArr[k-1] and k > 0:
                k -= 1
        if newArr[l] == newArr[l+1]:
            while newArr[l] == newArr[l+1] and l < len(newArr)-1:
                l += 1
        toAdd = min(min(k*2+1,(len(newArr)-1-k)*2+1),min(l*2+1,(len(newArr)-1-l)*2+1))
        count += toAdd
    return count
