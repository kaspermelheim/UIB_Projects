package uke2;

import java.util.List;

public class ThreeSum {

	public int threesum(List<Integer> numbers) {
		int sum = 0;
		for (int i = 0; i < numbers.size(); i++) {
			int j = i+1; 
			int k = numbers.size()-1;
			while (j < k) {
				if (numbers.get(i) + numbers.get(j) + numbers.get(k) == 0) {
					sum += 1;
					j++;
					k--;
			    }
				else if (numbers.get(i) + numbers.get(j) + numbers.get(k) < 0) {
					j++;
				}
				else {
					k--;
				}
			}
		}
		return sum;
	}
}
