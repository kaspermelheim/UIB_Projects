package Lecture13;

import java.util.Iterator;

public class Range implements Iterator<Integer>, Iterable<Integer> {

	int numInts;
	int current;
	
	public Range(int numInts) {
		this.numInts = numInts;
		this.current = 0;
	}
	
	@Override
	public boolean hasNext() {
		return current < numInts;
	}

	@Override
	public Integer next() {
		int next = current;
		current++;
		return next;
	}

	@Override
	public Iterator<Integer> iterator() {
		return new Range(this.numInts);
	}
	
	public static Iterable<Integer> range(int max) {
		return new Range(max);
	} 

}
