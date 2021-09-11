package uke1;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Josephus {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int M = sc.nextInt();
		int N = sc.nextInt();
		
		Queue<Integer> queue = new LinkedList<>();
		for(int i = 1; i < N; i++) {
			queue.add(i);
		}
		queue.add(0);
		
		while(!queue.isEmpty()) {
			System.out.printf("%d ", queue.poll());
			if(queue.isEmpty()) {
				break;
			}
			
			for (int i = 1; i < M; i++) {
				queue.add(queue.poll());
			}
		}

	}

}
