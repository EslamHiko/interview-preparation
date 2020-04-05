'''
Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to least frequently mentioned.

The comparison of strings is case-insensitive. If keywords are mentioned an equal number of times in reviews, sort alphabetically.

Example 1:

k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]

Output:
["anacell", "betacellular"]

Explanation:
"anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.
Example 2:

Input:
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

Output:
["betacellular", "anacell"]

Explanation:
"betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews, but "anacell" is lexicographically smaller.
Related problems:

https://leetcode.com/problems/top-k-frequent-words/
https://leetcode.com/problems/top-k-frequent-elements/
'''
import collections

def mySol(k,keywords,reviews):
    wordCount = {}
    for review in reviews:
        for word in review.split():
            if wordCount.get(word.lower()):
                wordCount[word.lower()] += 1
            else:
                wordCount[word.lower()] = 1
    sols = []
    for keyword in keywords:
        if wordCount.get(keyword):
            sols.append(keyword)

    sols.sort(key=lambda x: wordCount[x])
    sols.reverse()
    finalSol = []
    curr = 0
    while k != 0:
        if curr == len(sols)-2:
            if wordCount[sols[curr]] == wordCount[sols[curr+1]]:
                if sols[curr][0] < sols[curr+1][0]:
                    finalSol.append(sols[curr])
                else:
                    finalSol.append(sols[curr+1])
            else:
                finalSol.append(sols[curr])
        else :
            finalSol.append(sols[curr])
        curr += 1
        k -= 1
    return finalSol

print(mySol(2,["anacell", "cetracular", "betacellular"],[
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]))

print(mySol(2,["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"],[
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]))

# order matters
def mySolPRQueue(k,keywords,reviews):
    wordCount = {}
    for review in reviews:
        for word in review.split():
            if wordCount.get(word.lower()):
                wordCount[word.lower()] += 1
            else:
                wordCount[word.lower()] = 1
    sols = []
    wordsCopy = keywords.copy()
    wordsCopy = list(set(wordsCopy))
    wordsCopy.sort()
    PR = {}
    for i in range(0,len(wordsCopy)):
        PR[wordsCopy[i]] = i

    keywords = list(set(keywords))
    for keyword in keywords:
        if wordCount.get(keyword):
            sols.append(keyword)

    sols.sort(key=lambda x: wordCount[x])
    sols.reverse()
    finalSol = []
    curr = 0
    while k != 0:
        if curr == len(sols)-2:
            if wordCount[sols[curr]] == wordCount[sols[curr+1]]:
                if PR[sols[curr]] < PR[sols[curr+1]]:
                    finalSol.append(sols[curr])
                else:
                    finalSol.append(sols[curr+1])
            else:
                finalSol.append(sols[curr])
        else :
            finalSol.append(sols[curr])
        curr += 1
        k -= 1
    return finalSol

print(mySolPRQueue(2,["anacell", "cetracular", "betacellular"],[
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]))

print(mySolPRQueue(2,["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"],[
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]))

def myFinalSol(k,keywords,reviews):
    fullString = ' '.join(reviews).lower()

    return [v[0] for v in sorted(collections.Counter(fullString.split(' ')).items(),key=lambda x: (-x[1],x[0])) if v[0] in keywords][:k]

print(myFinalSol(2,["anacell", "cetracular", "betacellular"],[
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]))

print(myFinalSol(2,["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"],[
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better deltacellular than deltacellular.",
]))


'''
692. Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
'''
def sol692(words,k):
    return [v[0] for v in sorted(collections.Counter(words).items(), key=lambda x:  (-x[1],x[0]))][:k]

'''
347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

def sol347(nums,k):
    return [t[0] for t in sorted(collections.Counter(nums).items(),key=lambda x: (-x[1],x[0]))][:k]
