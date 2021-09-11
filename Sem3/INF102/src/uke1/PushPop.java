package uke1;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class PushPop {
	
	static int nextInt = 0;

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		Stack<Integer> stack = new Stack<>();
		ArrayList<Integer> numbers = new ArrayList<>();
		for(int i = 0; i < 10; i++) {
			numbers.add(sc.nextInt());
		}
		
		for(int i : numbers) {
			while (stack.isEmpty() || stack.peek() != 1 || nextInt > 11) {
				stack.push(nextInt);
				nextInt++;
			}
			
			if(nextInt == 11) {
				System.out.println("Impossible");
				System.exit(0);
			}
			
			stack.pop();
		}
		
		System.out.println("Possible");

	}

}
