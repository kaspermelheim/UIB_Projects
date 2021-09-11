package Lecture2;

import java.util.Collections;
import java.util.List;

public class FastDuplicateFinder<ST extends Comparable<ST>> implements DuplicateFinder<ST> {

	@Override
	public <T extends ST> T findDuplicate(List<T> list) {

		//sort the list
		Collections.sort(list);

		//check if two consecutive elements are equal
		for(int i = 1; i< list.size(); i++) {
			if(list.get(i).equals(list.get(i-1)))
				return list.get(i);
		}

		return null;
	}
}