package uke2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CheckPairs {
	
	static List<Integer> list = new ArrayList<>();
	
	public CheckPairs() {
		this.list = list;
	}
	
	public List fillList() {
		List<Integer> newList = new ArrayList<>();
		newList.addAll(Arrays.asList(-5,-3,0,1,3,4,5));
		return newList;
	}
	
	public int countPairs(List<Integer> list) {
		int count = 0;
		
		for(Integer i : list) {
			for(Integer j : list) {
				
				if(i == 0 || j == 0) {
					continue;
				}
				if(i + j == 0) {
					count++;
				}
			}
		}
		return count/2;
	}

	public static void main(String[] args) {
		
		CheckPairs cp = new CheckPairs();
		List<Integer> list = cp.fillList();
		System.out.println(list);
		System.out.println(cp.countPairs(list));
	}
}
