package Lecture5;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class InsertionSort implements Sorter {

	@Override
	public <T extends Comparable<? super T>> void sort(List<T> list) {
		
		ArrayList<T> sortedList = new ArrayList<T>(list.size());
		for(T t : list) {
			//hvis t finnes i listen returneres index til t
			//hvis t ikke finnes i listen returneres -insertionPoint
			int index = Collections.binarySearch(sortedList, t);
			if(index < 0) {
				index = -index-1;
			}
			sortedList.add(index,t);
		}
		Collections.copy(list, sortedList);

	}

}
