//
function howManyParantheisisToBeRemoved(str){
  var open = 0;
  var toRemove = 0;
  str.split('').forEach(char=>{
    if(char == '('){
      open++;
    } else {
      open--;
      if(open < 0){
        open = 0;
        toRemove++;
      }
    }
  });
  toRemove += open;
  console.log(toRemove);
}
//
//
// howManyParantheisisToBeRemoved("()())()");
// howManyParantheisisToBeRemoved("(()))()((");
// howManyParantheisisToBeRemoved(")(");

function largestDiversibleArr(arr){
  subArrs = [];
  maxArr = [];
  arr.forEach((el,index)=>{
      for(let i = 0; i < arr.length; i++){
        if(el % arr[i] == 0){
          if(!subArrs[index])
            subArrs[index] = [];
          subArrs[index].push(arr[i]);
        }
      }
      if(maxArr.length < subArrs[index].length){
        maxArr = subArrs[index];
      }
    }
  );
  console.log(maxArr)
  console.log(maxArr.length);
  return maxArr;
}
// largestDiversible([1, 16, 7, 8, 4]);
// largestDiversible([2, 4, 3, 8])
//

function longestDistinctElements(arr){
  mapForOccurances = [];
  mapForDistinctElements = [];
  maxArr = [];
  arr.forEach((el,index)=>
    {
      mapForOccurances[index] = [ ];
      mapForDistinctElements[index] = [ ];
      for(let i = index; i < arr.length; i++){
        if(mapForOccurances[index][arr[i]])
          break;

        mapForOccurances[index][arr[i]] = 1;
        mapForDistinctElements[index].push(arr[i]);
      }
      if(mapForDistinctElements[index].length > maxArr.length){
        maxArr = mapForDistinctElements[index];
      }
    }
  )
  console.log(maxArr)
  console.log(maxArr.length)
  return maxArr;
}
//
// longestDistinctElements([5, 1, 10, 3, 5, 11, 10, 2, 3, 4, 1])

// function canReachTheEnd(arr){
//   var i = 0;
//   while(1){
//     var moves = arr[i];
//     if(!moves) // has reached the end
//       break;
//     var max = arr[i+moves];
//     var maxIndex = i+moves;
//     for(j = moves; j > i; j--){
//       if(max < arr[j]){
//         max = arr[j];
//         maxIndex = j;
//       }
//     }
//     i = maxIndex;
//     if(arr[i] == 0) // can't reach the end
//       break;
//   }
//   console.log(i)
//   console.log(i >= arr.length - 1);
//
// }
//
// canReachTheEnd([1, 3, 1, 2, 0, 1])
// canReachTheEnd([1, 2, 1, 0, 0])


// How many are bigger than j1,j2 and lower than i1,i2

// function countSortedMatrix(matrix,i1,i2,j1,j2){
//   var rows = matrix.length;
//   var cols = matrix[0].length;
//   var remainingInTheLeftSide = cols - (cols - i2);
//   var remainingInTheRightSide = cols - (cols - j2 + 1);
//   var result = remainingInTheLeftSide  + cols * (i1) + remainingInTheRightSide + cols * (rows - j2 - 1);
//   console.log(result);
//   return result;
// }
//
// countSortedMatrix(
//   [[1, 3, 7, 10, 15, 20],
//  [2, 6, 9, 14, 22, 25],
//  [3, 8, 10, 15, 25, 30],
//  [10, 11, 12, 23, 30, 35],
//  [20, 25, 30, 35, 40, 45]],1,1,3,3);
//

/**
 * Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].
 */
// function getSubsets(arr){
//   var map = [];
//   var maxMap = [];
//   arr.forEach((el,index)=>{
//     map[index] = [];
//     for(let i = 0; i < arr.length; i++){
//       if(arr[i] % el == 0 || el % arr[i] == 0)
//         map[index].push(arr[i]);
//     }
//     if(maxMap.length < map[index].length){
//       maxMap = map[index];
//     }
//   });
//
//   console.log(maxMap);
//   return maxMap;
// }
//
// getSubsets( [3, 5, 10, 20, 21]);
// getSubsets( [1, 3, 6, 24]);

function returnPalindromes(str){

  var strings = [];
  for(let i = 0; i < str.length; i++){
    for(let j = i + 1; j < str.length + 1; j++){
      strings.push(str.slice(i,j));
    }
  }

  var palindromes = [];
  strings.forEach(string=>{
    if(isPalindrome(string)){
      palindromes.push(string)
    }
  });
  console.log((strings).reverse())
  palindromes.sort((a,b)=>{
    return a.length >= b.length ? -1 : 1;
  });
  console.log(strings.indexOf("kayak"))
  palindromes.forEach((word,index)=>{
    for(let i = palindromes.length - 1; i >= 0; i--){
      if(index == i)
        continue;
      if(word.indexOf(palindromes[i]) != -1){
        palindromes.splice(i,1)
        i--
      }
    }
  });
  console.log(palindromes)

  removeOverLappedPalindromes(str,palindromes);
  console.log(palindromes)
}

function removeOverLappedPalindromes(str,palindromes){
  var possibleLocations = [0]; // abc
  for(let i = 0; i < palindromes.length; i++){
    var currLocation = str.indexOf(palindromes[i]) + palindromes[i].length;
    possibleLocations.push(currLocation);
  }
  for(let i = 0; i < palindromes.length; i++){
    if(possibleLocations.indexOf(str.indexOf(palindromes[i])) == -1){
      palindromes.splice(i,1);
      i -= 1;
    }
  }
  return palindromes;
}

function isPalindrome(str){
  return str == str.split("").reverse().join("");
}

returnPalindromes("racecarannakayak")
