package inf101.v20.sem2.tools;

import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * This class main purpose is to implement an Iterator that iterates over a range of integers.
 * If you want to use Range in a for loop it also needs to implement Iterable.
 * We could probably have defined 2 classes to make it more clear what this class does
 * - Range implements Iterable<Integer>
 * - RangeIterator implements Iterator<Integer>
 * But it is also an example of how to implement 2 interfaces in the same class
 * @author mva021
 *
 */
public class Range implements Iterator<Integer>, Iterable<Integer> {

	int numInts; // the total number of integers to loop over
	int current; // the current position in the iterator
	
	/**
	 * The constructor creates the range: [0,1,2,... ,numInts-1]
	 * @param numInts
	 */
	public Range(int numInts) {
		this.numInts = numInts;
		this.current = 0;
	}
	
	@Override
	public boolean hasNext() {
		return current < numInts; //simply checks if we have reached the end
	}

	@Override
	public Integer next() { 
		if(!hasNext())
			throw new NoSuchElementException("Reached the end of the iterator.");
		int next = current;
		current ++;
		return next;
	}

	@Override
	public Iterator<Integer> iterator() {
		//creates a new iterator of the right size
		//important that new is used and not return e.g. "return this;" will not work 
		//Because if you want to iterate over the same range multiple times e.g. a double for loop
		//you need to restart at 0 and that is only done in the constructor
		return new Range(this.numInts); 
	}

	/**
	 * This method returns an Iterable<Integer> which can be used in a python style for loop.
	 * There is 2 possible ways to make this, the simples might be to return an ArrayList containing
	 * those numbers you want to iterate over (see commented out code).
	 * But here we choose to do a bit more elaborate solution by returning a new Range object
	 * @param max
	 * @return
	 */
	public static Range range(int max) {
			return new Range(max);
		}

}
