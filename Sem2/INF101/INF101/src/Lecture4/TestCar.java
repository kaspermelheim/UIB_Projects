package Lecture4;

import javax.swing.JOptionPane;

public class TestCar {

	public static void main(String[] args) {
		Car myCar = new Car("Mitsubishi", "Outlander");
		//myCar.honk();

		//Car[] cars = Car.readOrderFromFile("C:\Users\Kasper\OneDrive - University of Bergen\Documents\INF101\INF101\src\Lecture4\OneCarOrder.txt");
		
		
		Car[] cars = Car.readOrder();
		for(int i=0; i<cars.length; i++)
			System.out.println(cars[i]);
//		
		Car nybil = Car.inputCar();
		JOptionPane.showMessageDialog(JOptionPane.getRootFrame(), "En "+nybil.toString() + " har blitt laget!");
	}

}
