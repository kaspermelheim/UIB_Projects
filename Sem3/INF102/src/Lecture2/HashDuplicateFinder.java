package Lecture2;

import java.util.HashSet;
import java.util.List;

public class HashDuplicateFinder implements DuplicateFinder<Object> {

	@Override
	public <T> T findDuplicate(List<T> list) {
		//create a set to keep all items seen so far
		HashSet<T> set = new HashSet<T>(list.size());

		for(T item : list) {
			if(set.contains(item)) //if seen before
				return item;
			else
				set.add(item);
		}
		return null;
	}
}