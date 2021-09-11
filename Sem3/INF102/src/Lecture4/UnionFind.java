package Lecture4;

public interface UnionFind<E> extends Iterable<E> {

	public E find(E elem);
	
	public void union(E elem1, E elem2);
	
	public int count();
	
	public Iterable<E> group(E elem);
}
