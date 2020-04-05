function getAllSubSetsOfArr(arr){
  // [1,2,3,4,5] => [[1],[1,2],[1,2,3]...[1,2,3,4,5],[2],[2,3],...,[4,5],[5]]
  newArr = [];
  for(let i = 0; i < arr.length; i++){
    for(let j = i + 1; j < arr.length + 1; j++){
      newArr.push(arr.slice(i,j));
    }
  }
  return newArr;
}

console.log(getAllSubSetsOfArr([1,2,3,4,5]));
//
function getAllCombinations(arr){
var allCombinations = [];
var getCombinations = (current,rest)=>{
  for(let i = 0; i < rest.length; i++){
    // concat because we don't want to change current
    var currCombination = current.concat(rest[i]); // [1], [1,2], [1,2,3] => [1,2,3,4], [1,2,4]
    allCombinations.push(currCombination);
    var restOfTheArray = rest.slice(i+1);
    getCombinations(currCombination,restOfTheArray);
  }
}
getCombinations([],arr);
  return allCombinations;
}

function getCombinations(arr){
  combs = [];
  generateCombination = (curr,rest)=>{
    var currCombination = curr.concat(rest[0])
    combs.push(currCombination)
    rest.slice(i+1);
    generateCombination(currCombination,rest);
  }
  generateCombinations([],arr);
}
console.log(getAllCombinations([1,2,3,4]));
function minCoinChange(amount,coins){
  const store = new Array(amount+1).fill(amount+1)
  store[0] = 0;
  for(let total = 0; total <= amount; total++){
    for(let coin of coins){
        let remainder = total - coin;
        if(coin <= total){
          store[total] = Math.min(store[total],store[remainder]+1);
        }
      }
    }
    console.log(store)
    return store[amount]
}
// console.log(minCoinChange(5,[1,2,5]))
/*

I have two arrays:
var array1=["A","B","C"];
var array2=["1","2","3"];
How can I set another array to contain every combination of the above, so that:

var combos=["A1","A2","A3","B1","B2","B3","C1","C2","C3"];
 */
// function getAllCombos(arr1,arr2){
//   combos = [] //or combos = new Array(2);
//
//   for(var i = 0; i < arr1.length; i++)
//   {
//        for(var j = 0; j < arr2.length; j++)
//        {
//           //you would access the element of the array as array1[i] and array2[j]
//           //create and array with as many elements as the number of arrays you are to combine
//           //add them in
//           //you could have as many dimensions as you need
//           combos.push(arr1[i] + arr2[j])
//        }
//   }
//   return combos;
// }
// console.log(getAllCombos(["A","B","C"],[1,2,3]))
//

let binarySearch = function (arr, x, start, end) {
    if (start > end) return false;

    let mid=Math.floor((start + end)/2);

    if (arr[mid]===x) return true;

    if(arr[mid] > x)
        return recursiveFunction(arr, x, start, mid-1);
    else
        return recursiveFunction(arr, x, mid+1, end);
}

function brs(arr,target,start,end){
  if(start > end)return false;
  mid = Math.floor((start+end)/2)
  if(arr[mid] == target)return true;
  if(arr[mid] > x)
    return brs(arr,target,start,mid-1)
  else
  return brs(arr,target,mid+1,end)

}
function coinChangeWays(amount,coins){
  const ways = [];
  const sums = [];
  ways[0] = 1;
  for(coin of coins){
    for(let i = coin; i <= amount; i++){
      if(!ways[i])
        ways[i] = 0;
      ways[i] = ways[i] + ways[i-coin]
    }
  }
  console.log(ways)
  return ways[amount];
}
console.log(coinChangeWays(5,[1,2,5]));
