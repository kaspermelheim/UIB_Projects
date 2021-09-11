package Lecture11;

import java.util.Random;

public class DNA implements Comparable<DNA> {

	String sequence;
	
	public DNA(String sequence) {
		this.sequence = sequence;
	}
	
	public static DNA getRandom(int length) {
		Random rand = new Random();
		String sequence = "";
		
		for(int i = 0; i < length; i++) {
			char base = DNAgenerator.bases[rand.nextInt(4)];
			sequence += base;
		}
		return new DNA(sequence);
	}
	
	public String maxOccurence(int length) {
		//Generate all sequences
		DNAgenerator markers = new DNAgenerator(length);
		//Variable that stores best so far
		String best = null;
		int bestCount = 0;
		
		//Loop through all sequences
		for(String marker : markers.sequences) {
			
			//Find value for current marker
			int count = count(marker);
			
			//If current count greater than bestCount, set new best and bestCount
			if(count > bestCount) {
				best = marker;
				bestCount = count;
			}
		}
		return best;
	}
	
	public int count(String marker) {
		int count = 0;
		for(int startindex = 0; startindex < sequence.length(); startindex++) {
			if(sequence.substring(startindex).startsWith(marker)) {
				count++;
			}
		}
		return count;
	}
	
	@Override
	public String toString() {
		return "DNA: " + sequence;
	}
	
	@Override
	public boolean equals(Object obj) {
		if(obj instanceof DNA) {
			DNA other = (DNA) obj;
			return this.sequence.equals(other.sequence);
		}
		else {
			return false;
		}
	}

	@Override
	public int compareTo(DNA other) {
		return this.sequence.compareTo(other.sequence);
	}
}
