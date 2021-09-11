package Lecture2;

import java.util.AbstractList;

/**
 * Simple ArrayList only designed for String
 * @author Kasper
 *
 */

public class StringArrayList extends AbstractList<String> {
	
	String[] elements;
	int size;
	
	public StringArrayList() {
		elements = new String[10];
		int size = 0;
	}

	@Override
	public boolean add(String e) {
		add(size, e);
		return true;
	}
	
	public void add(int index, String element) {
		
		if(elements.length == size) {
			grow();
		}
		
		for(int i = size; i > index; i--) {
			elements[i] = elements[i-1];
		}
		elements[index] = element;
		size++;
	}
	
	/**
	 * Doubles the capacity
	 */
	
	private void grow() {
		String[] newElements = new String[size*2];
		for(int i = 0; i<size; i++) {
			newElements[i] = elements[i];
		}
		elements = newElements;
	}
	
	@Override
	public String set(int index, String element) {
		return elements[index] = element;
	}
	
	@Override
	public String get(int index) {
		return elements[index];
	}

	@Override
	public int size() {
		return size;
	}

}
