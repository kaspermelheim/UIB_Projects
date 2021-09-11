package uke1;

import java.util.Collections;
import java.util.List;

public class MyClosestPair implements ClosestPair {

	@Override
	public Pair findClosestPair(List<Double> list) {
		
		Collections.sort(list);
		Pair best = new Pair(Double.MAX_VALUE / 10, -Double.MAX_VALUE / 10);
		
		
		for(int i = 1; i < list.size(); i++) {
			Pair next = new Pair(list.get(i), list.get(i-1));
			if(next.difference() < best.difference());
		}
		
		return best;
	}

}
