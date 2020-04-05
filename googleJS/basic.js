/**
 * Notes:
 * arr.splice(i,1)=> remove element at i
 * arr.splice(i,0,x)=> adds x at position i
 * arr.sort((a,b)=>a>b ? -1 : a< b ?  1 : 0)
 */
function removeDuplicates(arr){
	var exists = [];
	for(let i = 0; i < arr.length; i++){
		if(exists[arr[i]]){
		    arr.splice(i,1);
        i--;
      } else {
        exists[arr[i]] = 1
      }
  }
  console.log(arr)
  return arr;
}
// //
// removeDuplicates([1,1,2,3,2,5,6,7,5,7,9,1])
//
function checkStrSub(str1,str2){
	var j = 0;
	for(let i = 0; i < str2.length; i++){
	   if(str2[i] == str1[j])
		   j++;
}
  return j == str1.length;
}
//
// console.log(checkStrSub("AXY", "ADXCPY"))
// console.log(checkStrSub("AXY", "YADXCP"))
//
//
// // descending order
// animals = [1,1,2,8,7,9,5,1,2,3]
// animals.sort(function (a, b) {
//     return a > b ? -1 : (a == b) ? 0 : 1;
// });
//
// console.log(animals)
// animals.sort()
// console.log(animals)

function checkForSum(arr,sum){
  var complimentsMap = {};
  var solutions = [];
  for(let i = 0; i < arr.length; i++){
    if(complimentsMap[arr[i]]){

      solutions.push([arr[i],complimentsMap[arr[i]]]);
    }
    var compliment = sum - arr[i];
    complimentsMap[compliment] = arr[i];
  }
  console.log(complimentsMap)
  console.log(solutions);
  return solutions;
}
//
// checkForSum([1,2,4,4,6],8)


/*
For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
 */
function getHowManyLessInTheRight(arr){
  var resultMap = {};
  for(let i = 0; i < arr.length;i++){
    resultMap[i] = 0;
    for(let j = i+1; j < arr.length; j++){
      resultMap[i] += arr[i] > arr[j] ? 1 : 0;
    }
  }
  console.log(resultMap)
  var resultArr = Object.keys(resultMap).map(key=>{
    return resultMap[key];
  });
  return resultArr;
}
// console.log(getHowManyLessInTheRight([3, 4, 9, 6, 1]))
//
function findDuplicate(arr){
  var hashMap = [];
  for(let i = 0; i < arr.length; i++){
    if(hashMap[arr[i]])
      return arr[i];
    else
      hashMap[arr[i]] = true;
  }
  return false;
}
// console.log(findDuplicate([1,2,3,4,5,6,7,8,9,10,11,6]))
// console.log(findDuplicate("acbbac"))

function mergeAndSort(arrays){
  let result = arrays[0];
  console.log(result)
  for(let i = 1; i < arrays.length; i++){
    for(let j = 0; j < arrays[i].length; j++){
      let element = arrays[i][j];
      for(let k = 0; k < result.length; k++){
        if(result[k] >= element){
          result.splice(k,0,element);
          break;
        }
        // if element is the biggest element then push it in the end
        if(k == result.length - 1){
          result.push(element);
          break;
        }
      }
    }
  }
  return result;
}

function mergeAndSortTwoArrays(arr1,arr2){
  result = [];
  i = 0;
  j = 0;
  // adds element until one of the arrays reach it's end
  while(i < arr1.length && j < arr2.length){
    if(arr1[i] < arr2[j]){
      result.push(arr1[i])
      i++;
    } else {
      result.push(arr2[j])
      j++;
    }
  }
  // adds elements which are left of the first array
  while(i < arr1.length){
    result.push(arr1[i])
    i++;
  }
  while(j < arr2.length){
    result.push(arr2[j])
    j++;
  }
  return result;
}
function mergeAndSortUsingTwo(arrays){
  let result = arrays[0];
  console.log(result)
  for(let i = 1; i < arrays.length; i++){
    result = mergeAndSortTwoArrays(result,arrays[i]);
  }
  return result;
}
// console.log(mergeAndSort([[5,7,9],[6,8,11],[1,2,3]]));
// console.log(mergeAndSortTwoArrays([5,7,9],[1,2,3]));
// console.log(mergeAndSortUsingTwo([[5,7,9],[6,8,11],[1,2,3]]));

function generateFib(n){
  memo = [];
  fib = (n)=>{
    if(memo[n])
      return memo[n];

    if(n <= 1)
      return 1;

    memo[n] = fib(n - 1) + fib(n - 2);
    return memo[n];
  }
  result = [0,1];
  for(let i = 1; i < n-1; i++){
    result.push(fib(i));
  }
  console.log(result);
}
// generateFib(20);

/*
given "11122" replace "12" -> "1"
given "abcbcbbccd" replace "bc" ->"ad"
*/
function replaceStringChars(string,toReplace,replaceWith){
  while(string.indexOf(toReplace) != -1){
    string = string.replace(toReplace,replaceWith);
  }
  return string;
}
// console.log(replaceStringChars("11122",'12','1'));
// console.log(replaceStringChars("abcbcbbccd",'bc','ad'));


//
function basicSliding(arr,k){
  let maxSum = 0;
  var result = [];
  var maxSumArr = [];
  for(let i = 0; i < arr.length - k +1; i++){
    var sum = arr[i];
    result[i] = [arr[i]];
    let temp = 1;
    while(temp <= k-1){
      sum += arr[temp+i];
      // console.log(sum)
      result[i].push(arr[temp+i]);
      temp++;
    }
    maxSum = Math.max(maxSum,sum);
    maxSumArr[sum] = result[i];
    // console.log(result[i])
  }
  return maxSumArr[maxSum];
}
// console.log(basicSliding([1,3,-1,-3,5,3,6,7],3))
//
function maxWindoSliding(arr,k){
  var result = [];
  for(let i = 0; i <= arr.length - k; i++){
    var currWindow = [];
    var temp = 0;
    while(temp < k){
      currWindow.push(arr[i+temp]);
      temp++;
    }
    var maxCurr = currWindow[0];
    for(let j = 1; j < currWindow.length; j++){
      if(maxCurr < currWindow[j])
        maxCurr = currWindow[j];
    }
    result.push(maxCurr);
  }
  return result;
}
//
// console.log(maxWindoSliding([1,3,-1,-3,5,3,6,7],3))

function makeAllZerosToTheRight(arr){
  var zeros = [];
  for(let i = 0; i < arr.length; i++){
    if(arr[i] == 0){
      zeros.push(i);
    } else {
      if(zeros.length){
        var pos = zeros.shift();
        [arr[i],arr[pos]] = [arr[pos],arr[i]];
        i--;
      }
    }

  }
  return arr;

}
console.log(makeAllZerosToTheRight([0,1,0,2,0,0,3,4]))
