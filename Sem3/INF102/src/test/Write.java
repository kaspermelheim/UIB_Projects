package test;

import java.util.concurrent.Semaphore;

public class Write implements Runnable {
	
	static Semaphore write = new Semaphore(1);
    
    @Override
    public void run() {
        try {
            write.acquire();
            System.out.println("Thread "+Thread.currentThread().getName() + " is writing.");
            Thread.sleep(2500);
            System.out.println("Thread "+Thread.currentThread().getName() + " has finished writing.");
            write.release();
        } catch (InterruptedException e) {
            System.out.println(e.getMessage());
        }
    }
}
