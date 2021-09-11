package Lecture12;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import Lecture11.DNA;
import Lecture11.DNAgenerator;

public class TestDNASorting {

	public static void main(String[] args) {
		DNAgenerator gen = new DNAgenerator(4);
		List<DNA> dnaList = new ArrayList<DNA>();
		for(String sequence : gen.getList()) {
			dnaList.add(new DNA(sequence));
		}
		
		Collections.shuffle(dnaList);
		System.out.println(dnaList);
		Collections.sort(dnaList, Collections.reverseOrder());
		System.out.println(dnaList);
		Collections.sort(dnaList, new DNAComparator());
		System.out.println(dnaList);

	}

}
