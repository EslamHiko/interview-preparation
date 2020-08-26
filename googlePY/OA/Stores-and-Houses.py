'''
You are given 2 arrays representing integer locations of stores and houses (each location in this problem is one-dementional). For each house, find the store closest to it.
Return an integer array result where result[i] should denote the location of the store closest to the i-th house. If many stores are equidistant from a particular house, choose the store with the smallest numerical location. Note that there may be multiple stores and houses at the same location.

Example 1:

Input: houses = [5, 10, 17], stores = [1, 5, 20, 11, 16]
Output: [5, 11, 16]
Explanation:
The closest store to the house at location 5 is the store at the same location.
The closest store to the house at location 10 is the store at the location 11.
The closest store to the house at location 17 is the store at the location 16.
Example 2:

Input: houses = [2, 4, 2], stores = [5, 1, 2, 3]
Output: [2, 3, 2]
Example 3:

Input: houses = [4, 8, 1, 1], stores = [5, 3, 1, 2, 6]
Output: [3, 6, 1, 1]
'''
def sol(houses,stores):
    result = []
    def nearestShop(house,stores):
        minDist = float('inf')
        nearestStore = stores[0]
        for store in stores:
            dist = abs(house-store)
            if minDist > dist:
                minDist = dist
                nearestStore = store
        return nearestStore
    for house in houses:
        result.append(nearestShop(house,stores))
    return result

print(sol([5, 10, 17],[1, 5, 20, 11, 16]))
print(sol([2, 4, 2],[5, 1, 2, 3]))
print(sol([4, 8, 1, 1],[5, 3, 1, 2, 6]))
