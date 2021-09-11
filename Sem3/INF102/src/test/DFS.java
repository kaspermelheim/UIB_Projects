package test;

public class DFS {

	public void DepthFirstSearch(Graph G, int s) {
		   marked = new boolean[G.V()];
		   edgeTo = new int[G.V()];
		   
		   for (int s : G.V()) {
		   	 if (!marked[v]) dfs(G, s);
		   }
		}
	
		private void dfs(Graph G, int v) {
		   marked[v] = true;
		   for (int w : G.adj(v)) {
		       if (!marked[w]) {
		           dfs(G, w);
				edgeTo[w] = v;
		       }
		   }
		}

}
