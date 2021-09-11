package test;

import java.util.Queue;

public class Semaphore {
	
	int num;
	Queue<Integer> queue;
	
	public void P(int num) { 
		//num er verdien til semafor
	    num = num - 1; 
	    if (num < 0) { 
	  
	        // add process to queue 
	        // here p is a process which is currently executing 
	        queue.push(p); 
	        block(); 
	    } 
	    else
	        return; 
	} 
	  
	V(Semaphore s) { 
	    s.value = s.value + 1; 
	    if (s.value <= 0) { 
	  
	        // remove process p from queue 
	        q.pop(); 
	        wakeup(p); 
	    } 
	    else
	        return; 
	}
}
