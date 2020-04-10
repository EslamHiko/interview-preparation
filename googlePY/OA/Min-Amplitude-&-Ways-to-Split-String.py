'''
Position: L3 New Grad
Location: Sunnyvale

I don't have the exact wording so I'll have to paraphrase

Question 1:
Given an Array A, find the minimum amplitude you can get after changing up to 3 elements. Amplitude is the range of the array (basically difference between largest and smallest element).

Example 1:

Input: [-1, 3, -1, 8, 5 4]
Output: 2
Explanation: we can change -1, -1, 8 to 3, 4 or 5
Example 2:

Input: [10, 10, 3, 4, 10]
Output: 0
Explanation: change 3 and 4 to 10
So the way I did it was sort it, and then start removing the end elements because we would only want to change a element to a number within the smallest amplitude. There are 4 options, remove all 3 from the end, remove 2 from end 1 from start, remove 1 from end and 2 from start, remove 3 from start. The runtime should be O(nlogn) since we used sort. I'm not sure if my logic is correct or maybe if we can do it in O(n)

Question 2:
Given a string S, we can split S into 2 strings: S1 and S2. Return the number of ways S can be split such that the number of unique characters between S1 and S2 are the same.

Example 1:

Input: "aaaa"
Output: 3
Explanation: we can get a - aaa, aa - aa, aaa- a
Example 2:

Input: "bac"
Output: 0
Example 3:

Input: "ababa"
Output: 2
Explanation: ab - aba, aba - ba
Looking back on this one I felt like I could've done better and got carried away about how easy I thought it was. I basically, looped from the second element to the second last element, had 2 sets, 1 for each half of the string. and then check if the size of the 2 sets are equal, if so increment a counter. The time complexity is O(n^2) since we have to iterate through the whole string to check of unique characters each time we split. and Space is O(n).
Is there a better way to do this?
'''

def solQ1(arr):

    if len(arr) <=4 : return 0
    arr.sort();
    minAmp = float('inf');
    for i in range(4):
        minAmp = min(minAmp, arr[len(arr)-1-i]-arr[3-i])

    return minAmp

print(solQ1([-1, 3, -1, 8, 5, 4]))
print(solQ1([10, 10, 3, 4, 10]))

def solQ2(arr):
    
    count = 0;
    for i in range(len(arr)):
        curr = arr[:i+1]
        rest = arr[i+1:]
        if len(set(curr)) == len(set(rest)):
            count += 1


    return count

print(solQ2("aaaa"))
print(solQ2("bac"))
print(solQ2("ababa"))
