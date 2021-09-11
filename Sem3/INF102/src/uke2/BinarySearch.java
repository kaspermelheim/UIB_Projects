package uke2;

import java.util.List;

public class BinarySearch implements BinarySearchI {

	@Override
	public <T extends Comparable<T>> int search(List<T> list, T item) {
		if (item.compareTo(list.get(0)) < 0) {
			return -1;
		}
		int low = 0; int high = list.size();
		while (low + 1 < high) {
			int mid = (low + high) / 2;
			if(item.compareTo(list.get(mid)) > 0) {
				high = mid;
			}
			else {
				low = mid;
			}
		}
		
		if(item.compareTo(list.get(low)) == 0) return low;
		else return -1;
		}

}
