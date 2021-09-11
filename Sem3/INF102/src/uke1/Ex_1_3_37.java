package uke1;

import java.util.LinkedList; 
import java.util.Queue;
import java.io.*; 


public class Ex_1_3_37 {
	  	
	static int josephus(int n, int k) { 
		if (n == 1) {
			return 1; 
		}
		else {
			return (josephus(n - 1, k) + k-1) % n + 1; 
		} 
	} 
	  
	public static void main(String[] args) { 
		System.out.println("The survivor sits in pos: " + josephus(8,2)); 
		
		//Amount of people in the queue
		int n = 8;
	        
        Queue<Integer> q = new LinkedList<Integer>();
        
        for (int i = 0; i < n; i++)
            q.add(i);
        
        int k = 0;
        
        while (!q.isEmpty()) {
        	
            int x = q.remove();
            
            if (++k % 2 == 0) {
                System.out.print(x+1 + " ");
            }
            else {
                q.add(x);
            }
        }
		} 
	} 
