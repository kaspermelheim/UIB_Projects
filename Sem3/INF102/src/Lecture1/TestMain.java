package Lecture1;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class TestMain {

	public static void main(String[] args) {
		
		ArrayList<String> navn = new ArrayList<>();
		
		navn.add("Jonas");
		navn.add("Ada");
		navn.add("Alvar");
		navn.add("Kasper");
		navn.add("Kasper");
		
		System.out.println(slowCheck(navn));
		System.out.println(fastCheck(navn));
		
		

	}
	
	public static Object slowCheck(List liste) {
		
		for(int i=0; i<liste.size() ; i++) {
			for(int j=0; j<i; j++) {
				
				if(liste.get(i).equals(liste.get(j))) {
					
					return "Minst en duplicate på: " + liste.get(i) + " i lista: " + liste;
				}
			}
		}
		return "Ingen duplicates i listen: " + liste;
	}
	
	public static Object fastCheck(List liste) {
		
		Collections.sort(liste);
		
		for(int i = 1; i < liste.size(); i++) {
			if(liste.get(i).equals(liste.get(i-1))) {
				return liste.get(i);
			}
		}
		return "Ingen duplicates i listen: " + liste;
	}
	
	

}
