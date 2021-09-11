package uke1;

import java.util.Stack;

public class Buffer implements BufferI{
	
	private Stack<Character> start = new Stack<>();
	private Stack<Character> end = new Stack<>();

	@Override
	public void insert(char c) {
		start.push(c);
		
	}

	@Override
	public char get() {
		return start.peek();
	}

	@Override
	public char delete() {
		return start.pop();
	}

	@Override
	public void left(int k) {
		k = Math.min(k,  start.size());
		for(int i = 0; i < k; i++) {
			end.push(start.pop());
		}
		
	}

	@Override
	public void right(int k) {
		k = Math.min(k,  end.size());
		for(int i = 0; i < k; i++) {
			start.push(end.pop());
		}
		
	}

	@Override
	public int size() {
		return start.size() + end.size();
	}

}
