package Lecture2;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Random;

public class StringListGenerator {
	/**
	 * Generates a List of random strings to be used for timing the different DuplicateFinder implementations
	 * @param n - size of the list generated
	 * @return - A list of n random strings
	 */
	public static List<String> generateStringList(int n) {
		List<String> list = new ArrayList<String>();
		//List<String> list = new LinkedList<String>();
		Random r = new Random();
		for(int i=0; i<n; i++) {
			list.add(generateRandomString(r));
		}
		return list;
	}

	/**
	 * @param r - The random used to create a ransom String
	 * @return - A random string of random length
	 */
	public static String generateRandomString(Random r) {
		int i;
		int len = r.nextInt(10)+10; //this line determines a length between 10 and 19 Characters
		StringBuffer sb = new StringBuffer(len);
		for(i=0;i<len;i++) {
			sb.append((char)('a'+r.nextInt(26)));
		}
		return sb.toString();
	}
}