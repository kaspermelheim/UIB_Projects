package Lecture4;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.Scanner;

import javax.swing.JOptionPane;

public class Car {

	private String make;
	private String model;

	//Constructor
	Car(String make, String model){
		this.make = make;
		this.model = model;
	}
	
	// input from GUI
	static Car inputCar() {
		String make = JOptionPane.showInputDialog("Hvilket merke ønsker du?");
		String model = JOptionPane.showInputDialog("Hvilket modell ønsker du?");		
		return new Car(make, model);
	}
	
	/**
	 * Reads in cars from a file
	 * @param filename
	 * @return
	 */
	static Car[] readOrderFromFile(String filename)
	{
		FileInputStream in = null;
		try {
			in = new FileInputStream(filename);
		} catch (FileNotFoundException e) {
			System.out.println("Vi valgte feil fil");
			e.printStackTrace();
		}
		
		return readOrder(in,false);
	}

	// reads an order from the terminal / keyboard
	static Car[] readOrder() {
		return readOrder(System.in,true);
	}
	
	static Car[] readOrder(InputStream in, boolean printQuestion) {
		// Make scanner
		Scanner inScanner = new Scanner(in);
		
		String firstLine = inScanner.nextLine();
		
		Scanner lineScanner = new Scanner(firstLine);
		String numCarstxt = lineScanner.next();
		int numCars = lineScanner.nextInt();
		Car[] cars = new Car[numCars];
		
		int index = 0;
		
		while(inScanner.hasNextLine()) {
			String line = inScanner.nextLine();
			
			if(line.isEmpty() ) {
				continue;
			}
			
			lineScanner = new Scanner(line);
			
			
			//Read one car
			String make = inScanner.next();
			String model = inScanner.next();
			int num = inScanner.nextInt();
			
			// Make car list
			for(int i=0; i<num; i++) {
				cars[index] = new Car(make, model);
				index++;
			}
		}
		
		//Lese fra input og printe ut i consoll
		
		/** if(printQuestion) {
			System.out.println("Hvilket merke ønsker du?");
		}
		String make = inScanner.next();

		if(printQuestion) {
			System.out.println("Hvilken modell ønsker du?");
		}
		String model = inScanner.next();
		
		if(printQuestion) {
			System.out.println("Hvor mange biler vil du ha?");
		}
		int num = inScanner.nextInt();

		Car[] cars = new Car[num];
		for(int i=0; i<num; i++) {
			cars[i] = new Car(make, model);
		} */
		
		return cars;
	}
	
	@Override
	public String toString() {
		return make + " "+model;
	}
	
	//public void honk() {
	//	Sound.play("C:\\INF101\\honk.wav");
	//}
}