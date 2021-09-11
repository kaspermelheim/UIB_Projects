package Lecture12;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class TestSorting {

	public static void main(String[] args) {
		int[] nums = {5,22,9,24,3,75,12};
		
		System.out.println(Arrays.toString(nums));
		Arrays.sort(nums);
		System.out.println(Arrays.toString(nums));
		
		int[] nums2 = {5,22,9,24,3,75,12};
		List<Integer> list = new ArrayList<Integer>();
		for(int i : nums2) {
			list.add(i);
		}
		
		System.out.println(list);
		Collections.sort(list);
		System.out.println(list);
	}

}
