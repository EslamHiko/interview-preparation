class PrefixMapSum {
  constructor(){
    this.map = [];
  }
  insert(str,key){
    this.map[str] = key;
    console.log(this.map)
  }
  sum(str){
    var sum = 0;
    Object.keys(this.map).forEach(key=>{
      if(key.indexOf(str) === 0){
        sum += this.map[key];
      }
    });
    console.log(sum);
    return sum;
  }
}

var mapsum = new PrefixMapSum();

mapsum.insert("columnar",3);
mapsum.insert("column",2);
mapsum.sum("col");
