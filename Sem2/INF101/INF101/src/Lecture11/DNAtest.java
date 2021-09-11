package Lecture11;

public class DNAtest {

	public static void main(String[] args) {
//		DNAgenerator gen = new DNAgenerator(3);
//		System.out.println("Found: "+gen.sequences.size());
//		System.out.println(gen.sequences);
		
		DNA dna = DNA.getRandom(300);
		System.out.println(dna);
		
		String marker = dna.maxOccurence(3);
		System.out.println(marker);
		System.out.println(dna.count(marker));
	}
}
