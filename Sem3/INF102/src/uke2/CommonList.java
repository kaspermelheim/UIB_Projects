package uke2;

import java.util.ArrayList;
import java.util.List;
import java.util.*;

public class CommonList {
	
	static List<Integer> list1 = new ArrayList<>();
	static List<Integer> list2 = new ArrayList<>();
	
	public CommonList() {
		this.list1 = list1;
		this.list2 = list2;
	}


	public List findDupes(List list1, List list2) {
		List<Integer> list3 = new ArrayList<>();
		
		for(int i = 0; i < list1.size(); i++) {
			for(int j = 0; j < list2.size(); j++) {
				if(list1.get(i) == list2.get(j)) {
					list3.add((Integer) list1.get(i));
				}
			}
		}
		return list3;
	}
	
	
	public static void main(String[] args) {
		
		CommonList cl = new CommonList();
		
		list1.add(1);
		list1.add(3);
		list1.add(7);
		list1.add(9);
		
		list2.add(0);
		list2.add(3);
		list2.add(8);
		list2.add(9);
		
		Collections.sort(list1);
		Collections.sort(list2);
		
		System.out.println(list1);
		System.out.println(list2);
		
		System.out.println(cl.findDupes(list1, list2));	
	}
}
