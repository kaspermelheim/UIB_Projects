package Lecture2;

import java.util.List;


/**
 * Interface for various implementations of duplicate finding 
 * @author Martin.Vatshelle@uib.no
 *
 * @param <ST> The type of arguments the list can contain
 */
public interface DuplicateFinder<ST> {

	/**
	 * @param <T>  - Type of elements
	 * @param list - A List of elements to search through
	 * @return	   - A duplicate element, if no such element exists, return null
	 */
	<T extends ST> T findDuplicate(List<T> list);
}
