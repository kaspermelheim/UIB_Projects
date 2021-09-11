package Lecture2;

import java.util.List;

public class DuplicateFinderTimer {
	
	public static void main(String[] args) {
		DuplicateFinder<Object> df1 = new SimpleDuplicateFinder();
		test(df1,20000);
		DuplicateFinder<String> df2 = new FastDuplicateFinder<String>();
		test(df2,20000);
		DuplicateFinder<Object> df3 = new HashDuplicateFinder();
		test(df3,20000);
		
	}

	/**
	 * Generates a list and times the execution of the findDuplicate on a list of Strings
	 * @param finder - the implementation to time
	 */
	public static void test(DuplicateFinder<? super String> finder,int n) {
		List<String> list = StringListGenerator.generateStringList(n);
		test(finder,list);
	}

	/**
	 * Times the execution of the findDuplicate on a list of Strings
	 * @param finder
	 * @param list
	 */
	public static <T> void test(DuplicateFinder<? super T> finder, List<T> list) {
		long start = System.currentTimeMillis();
		T duplicate = finder.findDuplicate(list);
		long stop = System.currentTimeMillis();
		System.out.println("Took "+(stop-start)+" ms to find "+duplicate);
	}



}