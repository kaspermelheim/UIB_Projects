package test;

import java.util.ArrayList;
import java.util.List;

public class Soking {
	
	public Soking() {
		
	}
	
	public List<Integer> partalList(List<Integer> list) {
		
		for(int i = 0; i <= 100; i=i+2) {
			list.add(i);
		}
		return list;
	}
	
	public List<Integer> oddList(List<Integer> list) {
		
		for(int i = 0; i <= 100; i=i+1) {
			list.add(i);
		}
		return list;
	}
	
	
	public static void main(String[] args) {
		
		ArrayList<Integer> tall = new ArrayList<>();
		
		Soking sok = new Soking();
		

	}

}
