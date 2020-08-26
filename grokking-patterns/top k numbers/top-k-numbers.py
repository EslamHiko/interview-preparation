'''
Problem Statement #
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
Example 2:

Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]
'''



def find_pairs_with_given_difference(arr, k):

  # 1. initialize the ht (needed) - with the complementary numbers - O(n) passing on the array and puttin gat the ht el => K+el
  # 2. passing on the array again - O(n)
  # 3. chacking if the complemetary of el exist at the ht
  # 3.a if exist put to result
  # 3.b if not continue
  # total: O(n) + O(n) = O(n)

  needed = {} # everything was in place
  result = []
  exists = {}
  for el in arr:
    if needed.get(k+el):
      needed[k+el].append(el)
    else:
      needed[k+el] = [el]
    # 0,k=1
    # -1
    # 0
    if needed.get(el-k):
      needed[el-k].append(el)
    else:
      needed[el-k] = [el]
    # x - y = k
    # x - k = y
  print(needed)
  for el in arr:
    if needed.get(el):
        for needed_el in needed[el]:
          if exists.get((el,needed_el)) is None and exists.get((needed_el,el)) is None:
            if el - needed_el == k:
              result.append([el,needed_el])
            else:
              result.append([needed_el,el])
          exists[(el,needed_el)] = 1
          exists[(needed_el,el)] = 1



  return result

function findPairsWithGivenDifference(arr, k):
    # since we don't allow duplicates, no pair can satisfy x - 0 = y
    if k == 0:
        return []

    map = {}
    answer = []

    for (x in arr):
        map[x - k] = x

    for (y in arr):
        if y in map:
            answer.push([map[y], y])

    return answer
