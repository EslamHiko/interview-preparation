/** Meeting hours problem **/
// https://interviewing.io/recordings/Javascript-Google-5
//
/*
1) Given a list of meeting objects
(e.g. {name: 'MeetingName', hours: numHours}) and an integer haveHours
denoting how many hours of one's schedule alloted to meetings,
write a function that optimizes the total number of meetings in one's day

2) Using the same input, write a function that optimizes the total number of hours one spends in meetings

{
  name: "",
  hours: 5
}
*/
function getMeetingsCombinations(meetings){
    var result = [];
    var getCombinations = (active,rest) => {
      for(let i = 0; i < rest.length; i++){
        var currCombination = active.concat(rest[i]);
        result.push(currCombination);
        var restOfMeetings = rest.slice(i+1);
        getCombinations(currCombination,restOfMeetings)
      }
    }
  getCombinations([],meetings);
  return result;
}
function solution(meetings, haveHours){
  // Getting all the combinations
  var result = getMeetingsCombinations(meetings);
  var sumMap = [];
  result.forEach(combination => {
    var sum = 0;
    combination.forEach((m)=>{
      sum += parseInt(m.hours);
    });
    if(!sumMap[sum] && sum <= haveHours){
      sumMap[sum] = [];
    }
    if(sum <= haveHours){
      sumMap[sum].push(combination);
    }
  });

  while(haveHours){
    if(sumMap[haveHours]){
      console.log(sumMap[haveHours]);
      break;
    }
    haveHours--;
  }

}

// solution([{hours:2},{hours:3},{hours:4},{hours:1}],5);

function longestSubSeq(s1,s2){
  var i = 0;
  var j = 0;
  var result1 = [];
  var result2 = [];
  var long,short;

  while(i < s1.length && j < s2.length){
    for(i = 0; i < s1.length; i++){
      var position = s2.indexOf(s1[i],j);
      if(position != -1){
        j = position + 1;
        result1.push(s1[i]);
      }
    }
  }
  i = 0;
  j = 0;
  while(i < s2.length && j < s1.length){
    for(i = 0; i < s2.length; i++){
      var position = s1.indexOf(s2[i],j);
      if(position != -1){
        j = position + 1;
        result2.push(s2[i]);
      }
    }
  }
  return [result1,result2];

}

console.log(longestSubSeq("ABBA","ABCABA"))
console.log(longestSubSeq("ABAZDC","BACBAD"))
console.log(longestSubSeq("AGGTAB","GXTXAYB"))

console.log(longestSubSeq("aaaa","aa"))



function lis(arr){
  var res = [];
  var maxSum = 0;
  var maxSumMap = [];
  var returnIncreasingSubs = (arr,indexItem,start) => {
    var curr = arr[indexItem];
    result = [curr];

    for(let i = start; i < arr.length; i++){


      if(curr < arr[i]){
        curr = arr[i];
        result.push(arr[i])
      }

    }
    if(maxSum < result.length)
      maxSum = result.length;
    if(!maxSumMap[result.length])
      maxSumMap[result.length] = []
    maxSumMap[result.length].push(result);
    return result;
  }
  for(let i = 0; i < arr.length; i++){
    res[i] = [];
    for(let j = i+1; j < arr.length; j++){
      res[i].push(returnIncreasingSubs(arr,i,j))
    }
  }
  console.log(maxSumMap)
  console.log(maxSumMap[maxSum])
  return res;
}
//
// console.log(lis([3, 2, 6, 4, 5, 1]))
// solve([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
