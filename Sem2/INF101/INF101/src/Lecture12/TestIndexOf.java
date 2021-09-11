package Lecture12;

import java.util.ArrayList;
import java.util.List;

import Lecture11.DNA;

public class TestIndexOf {

	public static void main(String[] args) {
		DNA dna1 = new DNA("ATCGTCA");
		DNA dna2 = new DNA("ATCGTCA");
		
		ArrayList<DNA> list = new ArrayList<DNA>();
		list.add(dna1);
		list.add(dna2);
		System.out.println(list.indexOf(dna1));
		System.out.println(list.indexOf(dna2));
		System.out.println(dna1.equals(dna2));
		System.out.println(dna1 == dna2);

		String txt1 = "Hello";
		String txt2 = "Hello";
		System.out.println(txt1.equals(txt2));
		System.out.println(txt1 == txt2);
	}
}
