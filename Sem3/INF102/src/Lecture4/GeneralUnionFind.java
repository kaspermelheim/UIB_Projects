package Lecture4;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;

public class GeneralUnionFind<E> implements UnionFind<E> {
	
	HashMap<E, E> parents;
	HashMap<E, Integer> sizes;
	int count;
	
	public GeneralUnionFind(Iterable<E> elements) {
		parents = new HashMap<E,E>();
		sizes = new HashMap<E, Integer>();
		for(E e : elements) {
			parents.put(e, null);
			sizes.put(e, 1);
		}
		
		count = parents.size();
	}
	
	public int groupSize(E elem) {
		return sizes.get(find(elem));
	}

	@Override
	public Iterator<E> iterator() {
		return parents.keySet().iterator();
	}
	
	E parent(E e) {
		return parents.get(e);
	}
	
	@Override
	public E find(E elem) {

		E current = elem;
		while(parent(current) != null) {
			current = parent(current);
		}
		E root = current;
		
		//Do path compression
		current = elem;
		while(parent(current) != null && !parent(current).equals(root) ) {
			E p = parent(current);
			parents.put(current, root);
			int totSize = sizes.get(p) - sizes.get(current);
			sizes.put(p, totSize);
			current = p;
		}
		return root;
	}

	@Override
	public void union(E elem1, E elem2) {
		
		E root1 = find(elem1);
		E root2 = find(elem2);
		
		if(!root1.equals(root2)) {
			int totSize = sizes.get(root1) + sizes.get(root2);
			if(groupSize(root1) > groupSize(root2)) {
				parents.put(root2, root1);
				sizes.put(root1, totSize);
			}
			
			else {
				parents.put(root1, root2);
				sizes.put(root1, totSize);
			}
			count--;
		}
	}

	@Override
	public int count() {
		return count;
	}

	@Override
	public Iterable<E> group(E elem) {
		ArrayList<E> group = new ArrayList<E>();
		E root = find(elem);
		
		for(E e : this) {
			if(find(e).equals(root)) {
				group.add(e);
			}
		}
		return null;
	}

}
