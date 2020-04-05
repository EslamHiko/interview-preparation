
/*
[[1], [2, 3], [1, 5, 1]] (1+3+5)
*/

function solveTheTriangle(arr){
  /** buttom to top **/
  for(let i = arr.length - 2; i >= 0; i--){
    for(let j = 0; j <= i; j++){
      arr[i][j] += Math.max(Math.max(arr[i+1][j],arr[i+1][j+1]),(arr[i+1][j+2] || 0));
    }
  }
  console.log(arr[0][0])
  return arr[0][0];
}
//
//
solveTheTriangle([
     [1],
    [2, 3],
   [1, 5, 1],
  [2,5,6,1,5]]);

/*
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.



Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").


Constraints:

1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] are English lowercase letters.
 */
var minFrequency = (singleQuery) => {
    let smallQueriesCount = [];
    let singleStringCharsCount = [];
    var minChar = singleQuery[0];
    for(let j = 0; j < singleQuery.length; j++){
        singleStringCharsCount[singleQuery[j]] = singleStringCharsCount[singleQuery[j]] ? singleStringCharsCount[singleQuery[j]] + 1 : 1;
        if(minChar > singleQuery[j])
            minChar = singleQuery[j];
    }
    var minFreq = singleStringCharsCount[minChar];

    return minFreq;

}

/**
 * @param {string[]} queries
 * @param {string[]} words
 * @return {number[]}
 */
var numSmallerByFrequency = function(queries, words) {
    let result = [];
    let lengthIndices = {};
    for(let i = 0; i < words.length; i++){
        var index = minFrequency(words[i]);
        lengthIndices[index] = lengthIndices[index] ? lengthIndices[index] + 1 : 1;
    }
    for(let i = 0; i < queries.length; i++){
        var minFreq = minFrequency(queries[i]);

        var count = 0;

        for(j of Object.keys(lengthIndices)){
            if(j > minFreq)
                count = count + lengthIndices[j];
        }
        result.push(count);
    }
    return result;
};

// console.log(numSmallerByFrequency(["bbb","cc"],["a","aa","aaa","aaaa"]))
// console.log(numSmallerByFrequency(["cbd"],["zaaaz"]))
/**
 * Target Sum
 *
 * You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
 * Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
 *
 * Find out how many ways to assign symbols to make sum of integers equal to target S.
 *
 * Example 1:
 *
 * Input: nums is [1, 1, 1, 1, 1], S is 3.
 * Output: 5
 *
 * Explanation:
 *
 * -1+1+1+1+1 = 3
 * +1-1+1+1+1 = 3
 * +1+1-1+1+1 = 3
 * +1+1+1-1+1 = 3
 * +1+1+1+1-1 = 3
 *
 * There are 5 ways to assign symbols to make the sum of nums be target 3.
 *
 * Note:
 * The length of the given array is positive and will not exceed 20.
 * The sum of elements in the given array will not exceed 1000.
 * Your output answer is guaranteed to be fitted in a 32-bit integer.
 */
const findTargetSumWays_I = (nums, target) => {
  const result = [];
  backtracking(nums, target, 0, 0, [], result);
  return result.length;
};
//
const backtracking = (nums, target, index, sum, solution, result) => {
  if (index === nums.length) {
    if (sum === target) {
      result.push(solution.slice());
    }
    return;
  }

  solution.push(nums[index]);
  backtracking(nums, target, index + 1, sum + nums[index], solution, result);
  solution.pop();

  solution.push(-nums[index]);
  backtracking(nums, target, index + 1, sum - nums[index], solution, result);
  solution.pop();
};


/**
* Best Time to Buy and Sell Stock
*
* Say you have an array for which the i-th element is the price of a given stock on day i.
*
* If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
* design an algorithm to find the maximum profit.
*
* Note that you cannot sell a stock before you buy one.
*
* Example 1:
*
* Input: [7,1,5,3,6,4]
* Output: 5
* Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
*              Not 7-1 = 6, as selling price needs to be larger than buying price.
*
* Example 2:
*
* Input: [7,6,4,3,1]
* Output: 0
* Explanation: In this case, no transaction is done, i.e. max profit = 0.
*/


// const maxProfit = prices => {
//   if (!prices) {
//     return 0;
//   }
//
//   let profit = 0;
//   let min = prices[0];
//
//   for (let i = 1; i < prices.length; i++) {
//     profit = Math.max(profit, prices[i] - min);
//     min = Math.min(min, prices[i]);
//   }
//
//   return profit;
// };
//
//
// function nQueen(newBoard,col = 0)
// {
//
//     solutions = [];
//     if (col == N){
//       console.log(newBoard);
//         return newBoard;
//       }
//
//
//
//     for (var i = 0; i < N; i++)
//     {
//         /* Check if the queen can be placed on
//           board[i][col] */
//         if ( isSafe(newBoard,i, col) )
//         {
//
//             /* Place this queen in board[i][col] */
//             newBoard[i][col] = 1;
//
//             /* recur to place rest of the queens */
//             if ( solveBoard(newBoard,col + 1) )
//                 return newBoard;
//
//             /* If placing queen in board[i][col]
//                doesn't lead to a solution, then
//                remove queen from board[i][col] */
//             newBoard[i][col] = 0; // BACKTRACK
//         }
//     }
//
//     return false;
// }
//
// function isSafe(newBoard, row, col){
//
//   // Checks the ← direction
//   for(var i=0; i<col; i++){
//     if (newBoard[row][i] === 1) {
//       return false;
//     }
//   }
//
//   // Checks the ↖ direction
//   for(var i=row, j=col; i>=0 && j>=0; i--, j--){
//     if (newBoard[i][j] === 1) {
//       return false;
//     }
//   }
//
//   // Checks the ↙ direction
//   for(var i=row, j=col; j>=0 && i<newBoard.length; i++, j--){
//     if (newBoard[i][j] === 1){
//       return false;
//     }
//   }
//
//   return true;
// }
