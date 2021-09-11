package uke1;

import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import org.junit.Test;

public class ClosestPairTest {

	private static ClosestPair getMyClosestPair() {
		//TODO: Here you need to call the constructor of your class
		return new MyClosestPair();
	}
	
	@Test
	public void testEqualElements() {
		ClosestPair cp = getMyClosestPair();
		for(int i=0; i<10; i++) {
			List<Double> list = generateRandomDoubleList(10);
			testEqualElements(cp,list);
		}
	}

	@Test
	public void testPairs() {
		ClosestPair cp = getMyClosestPair();
		for(int i=0; i<10; i++) {
			List<Double> list = generateRandomDoubleList(10);
			testPairs(cp,list);
		}
	}

	/**
	 * Checks that all pairs of different elements yield a higher difference than the answer returned.
	 * @param cp - The implementation to test
	 * @param list - The list to be used as input
	 */
	private static void testPairs(ClosestPair cp, List<Double> list) {
		Pair closest = cp.findClosestPair(list);
		System.out.println(list);
		System.out.println("Closest "+closest);
		for(Double a : list) {
			for(Double b : list) {
				Pair cur = new Pair(a,b);
				System.out.println(cur);
				if(cur.difference()>0)
					assertTrue(cur.difference()>=closest.difference());
			}
		}
	}

	/**
	 * Assumes input contains no duplicates, then adds a duplicate and assures the difference now is 0.
	 * @param cp - The implementation to test
	 * @param list - a list of random elements, hence no two elements are equal
	 */
	private static void testEqualElements(ClosestPair cp, List<Double> list) {
		Pair p = cp.findClosestPair(list);
		assertTrue(p.difference()>0);
		list.add(list.get(3));
		p = cp.findClosestPair(list);
		assertTrue(p.difference()==0);
		list.remove(list.size()-1);
	}

	/**
	 * Generates a List of random double values uniformly distributed between 0 and 1
	 * @param n - number of elements in the list
	 * @return A List of n random double values
	 */
	private static List<Double> generateRandomDoubleList(int n) {
		List<Double> list = new ArrayList<Double>();
		Random r = new Random();
		for(int i = 1; i<n; i++) {
			list.add(r.nextDouble());
		}
		return list;
	}
}
