/** Ugly Numbers / Regular Numbers **/
function isRegular(N){
  var result = maxDivide(N,2);
  result = maxDivide(result,3);
  result = maxDivide(result,5);
  return result == 1;
}
function maxDivide(N,divisor){
  while(N % divisor == 0)
    N = N / divisor;
  return N;
}
function regularNumbers(N){
  var curr = 1;
  var numbers = [curr];
  for(let i = 1; i < N; i++){
    while(1){
      curr++;
      if(isRegular(curr)){
        numbers.push(curr);
        break;
      }
    }
  }
  console.log(curr);
  console.log(numbers)
  return curr;
}
regularNumbers(3) // 8
regularNumbers(15) // 24
