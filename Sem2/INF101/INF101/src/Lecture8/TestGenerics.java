package Lecture8;

public class TestGenerics {

	public static void main(String[] args) {
		
		double a = 7.2;
		double b = 5.3;
		//int largest = max(a,b);
		//System.out.println(largest);
		
		System.out.println(max(a,b));
		String lastInAlphabet = maxGeneric("Martin", "Anna");
		System.out.println(lastInAlphabet);
		
		String largest = maxGeneric("Martin", "Anna");
		int highest = maxGeneric(12,23);
		System.out.println(largest + highest);
		
	}
	
	public static <Type extends Comparable<Type>> Type maxGeneric(Type input1, Type input2) {
		if(input1.compareTo(input2) >= 0) {
			return (Type) input1;
		}
		else {
			return (Type) input2;
		}
	}
	
	public static Comparable max(Comparable input1, Comparable input2) {
		if(input1.compareTo(input2) >= 0) {
			return input1;
		}
		else {
			return input2;
		}
	}
	
//	public static int max(int input1, int input2) {
//		if(input1 >= input2) {
//			return input1;
//		}
//		else {
//			return input2;
//		}
//	}

}
