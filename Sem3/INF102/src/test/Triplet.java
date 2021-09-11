package test;

import java.util.ArrayList;
import java.util.Collections;

public class Triplet implements ITriplet {

	@Override
	public <T> T threeEqual(ArrayList<T> list) {
		
		int num = 0;
	    for (T item : list) {
	    	if(Collections.frequency(list, item) == 3) {
	    		return item;
	    	}
	    }
		return null;
	}
	
	public static void main (String[] args) {
		Triplet t = new Triplet();
		ArrayList<Integer> liste = new ArrayList<>();
		liste.add(1);
		liste.add(2);
		liste.add(2);
		liste.add(4);
		liste.add(1);
		liste.add(4);
		liste.add(4);
		liste.add(5);
		System.out.println(t.threeEqual(liste));
		
	}

	/**
	 * @param <T> - Type of elements in the list
	 * @param list - a list of elements
	 * @return return -	an element that occurs at least 3 times in the list, 
	 * 					null if no such element exist
	 * 
	 */
	
}