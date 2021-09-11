package Lecture2;


import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class SetDuplicateFinder implements DuplicateFinder<Object> {

	/**
	 *	Total kj�retid O(n) (amortised)
	 */
	@Override
	public <T extends Object> T findDuplicate(List<T> list) {
		//contains all elements seen previously in the List
		Set<T> seenSoFar = new HashSet<T>(); //O(1)
		
		for(T t : list) { //iterates n times
			if(seenSoFar.contains(t)) { //if t has been seen earlier O(1)
				return t; //O(1)
			}else {
				seenSoFar.add(t); //if t has not been seen earlier O(1) in average
			}
		}
		return null;
	}

}