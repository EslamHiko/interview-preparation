arr = []
finalOutPut = ""

def processInput(arr,finalOutPut):
    n = int(input())
    emptySpace = input()
    for i in range(n):
        target = int(input())
        emptySpace = input()
        dims = [int(el) for el in input().split()]
        emptySpace = input()
        for j  in range(dims[0]): # columns
            arr.append([int(el) for el in input().split()])

        emptySpace = input()
        finalOutPut += searchArr(i,arr,target,finalOutPut)

        arr = []

    print(finalOutPut)



def searchArr(index,arr,target,finalOutPut):
    for i in arr:
        for j in i:
            if j == target:
                return 'Case #'+str(index)+': true\n'
                return
    return 'Case #'+str(index+1)+': false\n'


processInput(arr,finalOutPut)
