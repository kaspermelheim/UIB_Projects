package Lecture13;

import java.util.ArrayList;

public class TestClothing {

	public static void main(String[] args) {
		
		Runners myShoes = new Runners();
		Boots otherShoes = new Boots();
		//ArrayList<IShoes> list = new ArrayList<IShoes>();
		ArrayList<IClothing> list = new ArrayList<IClothing>();
		list.add(otherShoes);
		list.add(myShoes);
		System.out.println(list);
		
		IClothing item = list.get(1);
		System.out.println(item +" is an IClothing: "+(item instanceof IClothing));
		System.out.println(item +" is an IShoes:  "+(item instanceof IShoes));
		System.out.println(item +" is a Runners:  "+(item instanceof Runners));
		System.out.println(item +" is a Boots:  "+(item instanceof Boots));
	}	
}
