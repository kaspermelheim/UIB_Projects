package Lecture5;

import java.util.Iterator;
import java.util.function.Consumer;

public class Alphabet implements Iterator {
	
	
	public static void main(String[] args) {
		Alphabet abc = new Alphabet();
		
		while(abc.hasNext()) {
			System.out.print(abc.next()+" ");
		}
	}
	
	char currentChar;
	
	Alphabet() {
		currentChar = 'a';
	}
	
	@Override
	public boolean hasNext() {
		return currentChar <= 'z';
	}

	@Override
	public Object next() {
		char nextChar = currentChar;
		currentChar++;
		return nextChar;
	}	


}
