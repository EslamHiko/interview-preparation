'''
ref : https://leetcode.com/discuss/interview-question/352459/
'''

def sol(arr,k):
    max = ''
    for i in range(len(arr)):
        for j in range(i+k,len(arr)+1):
            subArr = ''.join([str(el) for el in arr[i:j]])
            if max < subArr:
                max = subArr

    return [int(el) for el in list(max)]

print(sol([1,4,3,2,5],4))
