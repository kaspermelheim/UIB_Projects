package uke3;

import java.util.ArrayList;
import java.util.List;

public class QuickSelect implements QuickSelectI{

	@Override
	public <T extends Comparable<? super T>> T findKth(List<T> list, int k) {
		if(k < 1) throw new IllegalArgumentException();
		T pivot = list.get(0);
		ArrayList<T> start = new ArrayList<>();
		ArrayList<T> end = new ArrayList<>();
		for (int i = 1; i < list.size(); i++) {
			if (list.get(i).compareTo(pivot) < 0) start.add(list.get(0));
			else end.add(list.get(i));
		}
		
		if(start.size() >= k) return findKth(start,k);
		else if (start.size() == k - 1) return pivot;
		else return findKth(end, k - start.size() - 1);
	}
	

}
