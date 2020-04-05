const fnon = (string) => {
  var map = {};
  console.log(string.split(''))
  string.split('').forEach(char => {
    if(map[char])
      map[char]++;
    else
      map[char] = 1;
  });
  console.log(map)
  var chars = Object.keys(map);
  console.log(chars);
  var sol = null;
  chars.forEach(char => {
    if(map[char] == 1){
      sol = char;
      return 0;
    }
  });
  return sol;
}


console.log(fnon("aacaabctb"))
