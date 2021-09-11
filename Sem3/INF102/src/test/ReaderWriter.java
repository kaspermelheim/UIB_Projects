package test;

import java.util.concurrent.Semaphore;

class ReaderWriter {

    public static void main(String[] args) throws Exception {
        Reader read = new Reader();
        Write write = new Write();
        Thread t1 = new Thread(read);
        t1.setName("Process1");
        Thread t2 = new Thread(read);
        t2.setName("Process2");
        Thread t3 = new Thread(write);
        t3.setName("Process3");
        Thread t4 = new Thread(read);
        t4.setName("Process4");
        
        t1.start();
        t3.start();
        t2.start();
        t4.start();
    }
}
