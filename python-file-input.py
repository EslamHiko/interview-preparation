f = open("input.txt", "r")
input = [el.replace('\n','') for el in f.readlines() if el != '\n']
currline = 0
n = int(input[currline])
finalOutPut = ''
def searchArr(index,arr,target,finalOutPut):
    for i in arr:
        for j in i:
            if j == target:
                return 'Case #'+str(index)+': true\n'
                return
    return 'Case #'+str(index+1)+': false\n'

for i in range(n):
    currline += 1
    target = int(input[currline])
    currline += 1
    dims = [int(el) for el in input[currline].split()]
    arr = []
    for j  in range(dims[0]): # columns
        currline += 1
        arr.append([int(el) for el in input[currline].split()])

    finalOutPut += searchArr(i,arr,target,finalOutPut)


f.close()
f = open('output.txt','w')
f.write(finalOutPut)
f.close()
