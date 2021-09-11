package uke2;

import java.util.Scanner;
import java.util.Stack;

public class ReversePolishNotation {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Stack<Integer> stack = new Stack<>();
		while(sc.hasNext()) {
			String token = sc.next();
			if(token.equals("+")) {
				Integer a = stack.pop() + stack.pop();
				stack.push(a);
			}
			else if (token.equals("*")) {
				Integer a = stack.pop() + stack.pop();
				stack.push(a);
			}
			else {
				Integer a = Integer.parseInt(token);
				stack.push(a);
			}
		}
		
		System.out.println(stack.pop());
	}
}
