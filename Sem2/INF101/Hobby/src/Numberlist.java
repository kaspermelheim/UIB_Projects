import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Numberlist {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		System.out.println("Vil skrive ut partal eller oddetall: ");
		String sjekk = input.nextLine();
		
		if("partal".equals(sjekk)) {
			System.out.println(toPartal(30));
		}
		else if("oddetall".equals(sjekk)) {
			System.out.println(toOdd(30));
		}
		else {
			System.out.println("Ugyldig input.");
		}
	}
	
	
	public static List<Integer> toPartal(int cap) {
		
		List<Integer> partal = new ArrayList<Integer>();
		for(int i = 0; i < cap; i++ ) {
			
			if(i % 2 == 0) {
				partal.add(i);
			}
		}
		return partal;
	}
	
	public static List<Integer> toOdd(int cap) {
		
		List<Integer> odd = new ArrayList<Integer>();
		for(int i = 0; i < cap; i++) {
			
			if(i % 2 != 0) {
				odd.add(i);
			}
		}
		return odd;
	}

}


