
class Node {
  constructor(value){
    this.value = value;
  }
}

/*
   a
  / \
 b   c
/ \  /
d   e f

*/

var tree = new Node('a');
tree.left = new Node('b');
tree.right = new Node('c');

tree.left.left = new Node('d');
tree.left.right = new Node('e');

tree.right.left = new Node('f');

// Traversals
console.log(tree.left.value)
function preOrder(node){
  if(!node)
    return;

console.log(node.value)
preOrder(node.left)
preOrder(node.right)

}

function inOrder(node){
  if(!node)
    return;

  inOrder(node.left)
  console.log(node.value)
  inOrder(node.right)
}
function postOrder(node){
  if(!node)
    return;

  postOrder(node.left)
  postOrder(node.right)
  console.log(node.value)
}

console.log(`
   a
  / \\
 b   c
/ \\  /
d   e f
`)
console.log("preOrder")
preOrder(tree);
console.log("inOrder")
inOrder(tree);
console.log("postOrder")
postOrder(tree);

function invertTree(tree){
  if(!tree)
    return;

  var right = invertTree(tree.right);
  var left = invertTree(tree.left);
  tree.left = right;
  tree.right = left;
  return tree;
}
function BFS(root){
  if(root == null)
    return;

  var q = [];
  q.push(root)
  while(q.length){
    node = (q.shift())

    console.log(node.value)
    if(node.left)
      q.push(node.left)

    if(node.right)
      q.push(node.right)
  }
}
const reversed = invertTree(tree);
/*
  a
 / \
 c  b
 \  / \
  f e  d
 */
console.log("preOrder Inverted")
preOrder(reversed)


function reconstructBinaryTreeFromPostOrder(arr){
    getTree = (seq)=>{
      var head = new Node(seq[seq.length - 1]);
      if(seq.length == 1)
        return head;

      var separator;
      for(let i = 0; i < seq.length - 1; i++){
        if(seq[i] > head.value){
          separator = i;
          break;
        }
      }
      var lessPart = seq.slice(0,separator)
      var greatPart = seq.slice(separator,seq.length-1);

      if(lessPart.length)
      head.left = getTree(lessPart);
      if(greatPart.length)
      head.right = getTree(greatPart);

      return head;
    }
    var tree = getTree(arr);
     console.log(tree)
     console.log(tree.value == 5)
     console.log(tree.left.value == 3)
     console.log(tree.right.value == 7)
     console.log(tree.left.left.value == 2)
     console.log(tree.left.right.value == 4)
     console.log(tree.right.right.value == 8)
    return tree;
}

reconstructBinaryTreeFromPostOrder([2, 4, 3, 8, 7, 5])
var tree = new Node('a');
tree.left = new Node('b');
tree.right = new Node('c');

tree.left.left = new Node('d');
tree.left.right = new Node('e');

tree.right.left = new Node('f');
BFS(tree)

var serializer = function(node, output) {
	if(!node){
		output.push('#');
		return;
	}
	output.push(node.val);
	serializer(node.left, output);
	serializer(node.right, output);

}


var deserialize = function(data) {

    data = data.split(',');
    var index = 0;
    function deserializer(data) {
       if(index > data.length || data[index] === '#'){
       	return null;
       }

       var node = new TreeNode(parseInt(data[index]));
       index++;
       node.left = deserializer(data,index);
       index++;
       node.right = deserializer(data, index);
       return node;
    }

    return deserializer(data);
};
