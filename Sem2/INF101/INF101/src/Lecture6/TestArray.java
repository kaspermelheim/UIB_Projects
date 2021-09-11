package Lecture6;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class TestArray {

	public static void main(String[] args) {
		
		String[] myList = new String[10];
		ArrayList<String> todoList = new ArrayList<String>(); // Valgfritt å sette lengd på list new ArrayList()
		todoList.add("Gå på forelesning");
		todoList.add("Gjør ukeoppgaver");
		
		System.out.println(todoList);
		
		String task2 = todoList.get(1);
		
		
		ArrayList<Integer> numSteps = new ArrayList<Integer>(366);
		
		int dag1 = 7500;
		numSteps.add(dag1);
		numSteps.add(9999);
		numSteps.add(4200);
		
		System.out.println("Antall dager registrert: " + numSteps.size());
		
		List<String> myList2 = new LinkedList<String>();
		myList2.add("Hello");
		myList2.add("World");
		int index = myList2.indexOf("Hello");
		System.out.println("Hello er ord nummer: " + index);
		
		//getPartal(numSteps);
		
		//For loops for å lage liste med tall, printe ut hvert element.
		
		ArrayList<Integer> models = new ArrayList<Integer>();
		
		for(int x = 0; x <= 10; x++) {
			models.add(x);
		}
		System.out.println("Original liste: "+models);
		
		/**Printer ut hvert element
		
		for(int i = 0; i < models.size(); i++) {
            System.out.println(models.get(i));
        }
		*/
		
		/**
		//Printer ut alle partal i en ny liste
		ArrayList<Integer> partal = new ArrayList<Integer>();
		
		for(int y = 0; y < models.size(); y = y + 2) {
			partal.add(models.get(y));
		}
		System.out.println("Liste med partal: " +partal);
		*/
		
		getPartalPos(models);
		getPartal(models);
		
	}
	
	//Method for å hente alle element i pos = partal fra liste
	static void getPartalPos(ArrayList<Integer> models) {
		
		//Printer ut alle partal i en ny liste
		ArrayList<Integer> partalPos = new ArrayList<Integer>();
		
		for(int y = 0; y < models.size(); y = y + 2) {
			partalPos.add(models.get(y));
		}
		System.out.println("Alle element med partal pos fra liste models: "+partalPos);
	  }
	
	static void getPartal(ArrayList<Integer> models) {
		
		ArrayList<Integer> partal = new ArrayList<Integer>();
		
		for(int i = 0; i < models.size(); i++ ) {
			
			if(models.get(i) % 2 == 0) {
				partal.add(models.get(i));
			}
		}
		System.out.println("Alle partal fra liste models: "+partal);
	}
}


