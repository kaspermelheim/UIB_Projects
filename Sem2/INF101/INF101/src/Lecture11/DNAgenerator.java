package Lecture11;

import java.util.ArrayList;
import java.util.List;

public class DNAgenerator {

	List<String> sequences;
	int length;
	static final char[] bases = {'A','C','G','T'};
	
	/**
	 * Constructor
	 * @param length
	 */
	public DNAgenerator(int length) {
		sequences = new ArrayList<String>();
		this.length = length;
		generate("");
	}
	
	public List<String> getList() {
		return sequences;
	}
	
	/**
	 * Generate all sequences of length = this.length() which starts with the string start
	 * @param start the first few letters in the sequence
	 */
	public void generate(String start) {
		if(length > start.length()) {
			for(char base : bases) {
				String next = start + base;
				//System.out.println("Calling generate with "+ next);
				generate(next);
			}
		}
		else {
			//System.out.println("Found: " +start);
			sequences.add(start);
		}
	}
}
