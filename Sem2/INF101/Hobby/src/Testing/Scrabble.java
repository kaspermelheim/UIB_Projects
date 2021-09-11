package Testing;

public class Scrabble {

	/**
	 * This method is used by the game Scrabble where the goal is to rearrange
	 * some of the given letters into a word.
	 * A letter in Scrabble is always upper case, this method accepts both upper and lower case letters
	 * and considers e.g. a lower case 'a' equal to an upper case 'A' 
	 * You may assume that all letters in input are valid letters in the English alphabet.
	 * 
	 * @param letters - the letters you have to your disposal
	 * @param word - the word you are trying to form
	 * @return true if it is possible to form the word by rearranging the letters, false otherwise
	 */
	public static boolean canMake(String letters, String word) {
		letters = letters.toUpperCase();
		word = word.toUpperCase();
		
		for(Character c:word.toCharArray()) {
			
			if(!letters.contains(c.toString())) {
				return false;
			}
			else {
				letters = letters.replaceFirst(c.toString(), "");
			}
		}
		return true;
	}
	
	
}
