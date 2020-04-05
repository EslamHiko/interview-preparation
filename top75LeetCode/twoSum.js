/*

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

*/
const sol = (arr,target) => {
  missing = {}
  indices = {}
  for(i in arr){
    if(missing[arr[i]] !== undefined)
      return [[i,indices[missing[arr[i]]],[arr[i],missing[arr[i]]]]];
    missing[target-arr[i]] = arr[i];
    indices[arr[i]] = i;
  }
}


console.log(sol([2, 7, 11, 15],9))
console.log(sol([0,4,3,0],0))
