package Lecture2;

import java.util.List;

/**
 * This implementation tests all pairs in a list to see if any pair is a duplicate
 * @author mva021
 *
 */
public class SimpleDuplicateFinder implements DuplicateFinder<Object> {

	@Override
	public <T> T findDuplicate(List<T> list) {

		//Loop through all pair of elements
		for(int i=0; i<list.size();i++) {
			for(int j=0; j<i; j++){

				// if two are equal, return one of those
				if(list.get(i).equals(list.get(j))) {
					return list.get(i);
				}
			}
		}

		//if no duplicate elements are found return null
		return null;
	}


}
