package test;

import java.util.ArrayList;

public interface ITriplet {

	/**
	 * @param <T> - Type of elements in the list
	 * @param list - a list of elements
	 * @return return -	an element that occurs at least 3 times in the list, 
	 * 					null if no such element exist
	 * 
	 */
	public <T> T threeEqual(ArrayList<T> list);
}