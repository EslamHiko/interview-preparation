
class Graph {
   constructor() {
      this.edges = {};
      this.nodes = [];
   }

   addNode(node) {
      this.nodes.push(node);
      this.edges[node] = [];
   }

   addEdge(node1, node2, weight = 1) {
      this.edges[node1].push({ node: node2, weight: weight });
      this.edges[node2].push({ node: node1, weight: weight });
   }

   addDirectedEdge(node1, node2, weight = 1) {
      this.edges[node1].push({ node: node2, weight: weight });
   }

   // addEdge(node1, node2) {
      //   this.edges[node1].push(node2);
      //   this.edges[node2].push(node1);
   // }

   // addDirectedEdge(node1, node2) {
      //   this.edges[node1].push(node2);
   // }

   display() {
      let graph = "";
      this.nodes.forEach(node => {
         graph += node + "->" + this.edges[node].map(n => n.node).join(", ") + "\n";
      });
      console.log(graph);
   }

   BFS(node){
     let q = [];
     let visited = [];
     q.unshift(node) // enqueue
     visited.add(node)
     while(q.length){
       let t = q.shift();
       console.log(t)
       this.edges[t].filter(n => !visited[n]).forEach(n => {
         visited[n] = 1; // marking it as visited
         q.unshift(n);
       })
     }
   }

   DFS(node){
     let s = [];
     let visited = [];
     s.push(node)

     while(s.length){
       let t = s.pop();

       console.log(t);
       // 1. In the edges object, we search for nodes this node is directly connected to.
        // 2. We filter out the nodes that have already been explored.
        // 3. Then we mark each unexplored node as explored and push it to the Stack.
        this.edges[t].filter(n => !visited[n]).forEach(n => {
           visited[n] = 1;
           s.push(n);
        });

     }
   }

   topologicalSortHelper(node, visited, s) {
     visited[node] = 1;
     this.edges[node].forEach(n => {
        if (!visited[n]) {
           this.topologicalSortHelper(n, visited, s);
        }
     });
     s.push(node);
  }

  topologicalSort() {
    // Create a Stack and add our initial node in it
    let s = [];
    let visited = [];
    this.nodes.forEach(node => {
       if (!visited[node]) {
          this.topologicalSortHelper(node, visited, s);
       }
    });
    while (!s.length) {
       console.log(s.pop());
    }
 }
}


function getStartPoint(matrix){
  for(let i = 0;i < matrix.length; i++){
    for(let j = 0; j < matrix[i].length; j++){
      if(matrix[i][j] == 's'){
        return [i,j];
      }
    }
  }
}
function isSafe(matrix,visited,x,y){
  return !(x < 0 || y < 0 || x >= matrix.length || y >= matrix[0].length || visited[x][y] || matrix[x][y] == '#')
}
function shortestPath(matrix){
  const start = getStartPoint(matrix);


  const dx = [-1,1,0,0]; // [-1,-1,0,1,1,1,0,-1]
  const dy = [0,0,1,-1]; // [0,1,1,1,0,-1,-1,-1]

  const visited = [];
  for(let i = 0; i < matrix[0].length; i++){
    visited[i] = [];
  }

  visited[start[0]][start[1]] = true;

  let queue = [[start[0],start[1]],null];

  let steps = 0;

  while(queue.length){
    var curr = queue.shift();

    if(curr){
      if(matrix[curr[0]][curr[1]] == 'e'){
        return steps;
      }
      for(let i = 0; i < dx.length; i++){
        const x = p[0] + dx[i];
        const y = p[y] + dy[i];

        if(isSafe(matrix,visited,x,y)){
          queue.push([x,y])
          visited[x][y] = true;
        }
      }
    } else {
      steps++;
      if(queue.length){
        queue.push(null);
      }
    }
  }
  return -1;
}
