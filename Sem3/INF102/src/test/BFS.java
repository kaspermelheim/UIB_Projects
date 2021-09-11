package test;

public class BFS {

	public void BreadthFirstPaths(Graph G, int s) {
	       marked = new boolean[G.V()];
	       distTo = new int[G.V()];
	       edgeTo = new int[G.V()];
	       bfs(G, s);
	   }

	private void bfs(Graph G, int s) {
	       Queue<Integer> q = new Queue<Integer>();
	       for (int v = 0; v < G.V(); v++)
	           distTo[v] = INFINITY;
	       distTo[s] = 0;
	       marked[s] = true;
	       q.enqueue(s);

	       while (!q.isEmpty()) {
	           int v = q.dequeue();
	           for (int w : G.adj(v)) {
	               if (!marked[w]) {
	                   edgeTo[w] = v;
	                   distTo[w] = distTo[v] + 1;
	                   marked[w] = true;
	                   q.enqueue(w);
	               }
	           }
	       }
	   }

}
