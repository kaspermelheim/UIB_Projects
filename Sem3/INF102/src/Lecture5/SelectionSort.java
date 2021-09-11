package Lecture5;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class SelectionSort implements Sorter {

	//O(n^2)
	@Override
	public <T extends Comparable<? super T>> void sort(List<T> list) {
		
		ArrayList<T> sortedList = new ArrayList<T>(); //O(n)
		
		while(!list.isEmpty()) { //O(n) ganger, totatl O(n^2)
			
			//find minimum element
			T min = Collections.min(list); //O(n)
			sortedList.add(min); //O(1)
			list.remove(min); //O(n)
		}
		
		list.addAll(sortedList); //O(n)

	}

}
