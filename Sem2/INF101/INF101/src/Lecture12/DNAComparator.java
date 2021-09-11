package Lecture12;

import java.util.Comparator;

import Lecture11.DNA;

public class DNAComparator implements Comparator<DNA> {

	@Override
	public int compare(DNA dna1, DNA dna2) {
		int count1 = dna1.count("C");
		int count2 = dna2.count("C");
		if(count1 == count2) {
			return dna1.compareTo(dna2);
		}
		else {
			return count2-count1;
		}
	}

}
