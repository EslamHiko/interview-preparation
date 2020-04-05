def removeDuplicates(arr):
    length = len(arr)
    map = {}
    final = []
    for i in range(0,length):
        if map.get(arr[i]):
            i -= 1
            length -= 1
        else:
            map[arr[i]] = 1
            final.append(arr[i])
    return final

def removeDuplicates2(arr):
    return list(dict.fromkeys(arr))

def removeDuplicates3(arr):
    return list(set(arr))

print(removeDuplicates([1,1,2,3,2,5,6,7,5,7,9,1]))
print(removeDuplicates2([1,1,2,3,2,5,6,7,5,7,9,1]))
print(removeDuplicates3([1,1,2,3,2,5,6,7,5,7,9,1]))

def checkStrSubOneAnother(str1,str2):
    j = 0
    if len(str1) > len(str2):
        str1,str2 = str2,str1

    for i in range(len(str2)):
        if str1[j] == str2[i]:
            j += 1

    return j == len(str1)

print(checkStrSubOneAnother("AXY", "ADXCPY"))
print(checkStrSubOneAnother("ADXCPY","AXY"))
print(checkStrSubOneAnother("AXY", "YADXCP"))
print(checkStrSubOneAnother("YADXCP","AXY"))
