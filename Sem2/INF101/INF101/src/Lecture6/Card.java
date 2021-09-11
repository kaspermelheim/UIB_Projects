package Lecture6;

import java.util.Arrays;
import java.util.List;

public class Card {

	static String[] names = {"Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
			"Knight", "Queen", "King"};
	
	static String[] suits = {"Spades", "Hearts", "CLubs", "Diamonds"};
	
	String suit;
	String value;
	
	public Card(String suit, String value) {
		
		List<String> al = Arrays.asList(names);
		
		if(!al.contains(value)) {
			throw new IllegalArgumentException(value + " is not a valid card.");
		}
		
		this.suit = suit;
		this.value = value;
	}
	
	public String getValueName() {
		return value;
	}

	public int getValue() {
		List<String> al = Arrays.asList(names);
		//Find the index of array
		//Returns number from 1 - 13
		return al.indexOf(value) +1;
	}

	@Override
	public String toString() {
		return value +" of "+suit;
	}
	
	
}
