
public class Methods {

	public static void main(String[] args) {
		//TODO
		
		System.out.println(pow(5,19));
	}

	public static int pow(int a, int b) {
		int[] result = new int[b+1];
		result[0] = 1;
		for(int i = 1; i<=b; i++) {  //i++ samme som i=i+1
			result[i] = result[i-1]*a;
		}
		
		for(int i=0; i<=b; i++) {
			System.out.println(a+"^"+i+" = " +result[i]);
			System.out.println("Java er kjempekult :) " + i);
		}
		
		return result[b];
		
	}
}
