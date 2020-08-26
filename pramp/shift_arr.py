def shifted_arr_search(shiftArr, num):
  pivot = findPivotPoint(shiftArr)

  if pivot == 0 or num < shiftArr[0]:
      return binarySearch(shiftArr, pivot, len(shiftArr) - 1, num)

  return binarySearch(shiftArr, 0, pivot - 1, num)


def findPivotPoint(arr):
  begin = 0
  end = len(arr) - 1

  while (begin <= end):
      mid = begin + int((end - begin)/2)
      if (mid == 0 or arr[mid] < arr[mid-1]):
          return mid
      if (arr[mid] > arr[0]):
          begin = mid + 1
      else:
          end = mid - 1

  return 0


def binarySearch(arr, begin, end, num):
  while (begin <= end):
      mid = begin + int((end - begin)/2)
      if (arr[mid] < num):
          begin = mid + 1
      elif (arr[mid] == num):
          return mid
      else:
          end = mid - 1

  return -1
