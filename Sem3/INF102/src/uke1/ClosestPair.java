package uke1;

import java.util.List;


/**
 * Interface for various implementations of duplicate finding 
 * @author Martin.Vatshelle@uib.no
 *
 * @param <ST> The type of arguments the list can contain
 */
public interface ClosestPair {

	/**
	 * This method should find the pair of elements in the list that has the least difference.
	 * @param <T>  - Type of elements
	 * @param list - A List of elements to search through
	 * @return	   - pair of closest element, null if size 0 or 1
	 */
	Pair findClosestPair(List<Double> list);
}