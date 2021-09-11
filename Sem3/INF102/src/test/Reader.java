package test;

import java.util.concurrent.Semaphore;

public class Reader implements Runnable {
	
	static int readNum = 0;
	static Semaphore read = new Semaphore(1);
	static Semaphore write = new Semaphore(1);
	
	
    @Override
    public void run() {
        try {
            //Hent seksjon
            read.acquire();
            readNum++;
            if (readNum == 1) {
                write.acquire();
            }
            read.release();

            //Les seksjon
            System.out.println(Thread.currentThread().getName() + " is reading.");
            Thread.sleep(1200);
            System.out.println(Thread.currentThread().getName() + " has finished the reading.");

            //Frigjør seksjon
            read.acquire();
            readNum--;
            
            if(readNum == 0) {
                write.release();
            }
            read.release();
        } catch (InterruptedException e) {
            System.out.println(e.getMessage());
        }
    }
}