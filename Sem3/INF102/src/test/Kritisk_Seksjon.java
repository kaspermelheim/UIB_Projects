package test;

import java.util.concurrent.*; 

//Will take Resource as  shared class
class Kritisk_Seksjon 
{ 
  static int count = 0; 
} 

class MyDemo extends Demo 
{ 
  Semaphore sem; 
  String threadName; 
  public MyDemo(Semaphore sem, String threadName) 
  { 
      super(threadName); 
      this.sem = sem; 
      this.threadName = threadName; 
  } 

  @Override
  public void run() { 
       
      // Run By X
      if(this.getName().equals("X")) 
      { 
          System.out.println("Starting " + threadName); 
          try
          { 
              // Will get the permit to access shared resource
              System.out.println(threadName + " waiting for a permit."); 
           
              // acquiring the lock 
              sem.acquire(); 
           
              System.out.println(threadName + " gets a permit."); 
       
              // Now, accessing the shared resource and rest will wait  
               
              for(int i=0; i < 7; i++) 
              { 
                  Resource.count++; 
                  System.out.println(threadName + ": " + Resouce.count); 
       
                   
                  // Now thread Y will try  to execute 
                  Thread.sleep(20); 
              } 
          } catch (InterruptedException exc) { 
                  System.out.println(exc); 
              } 
       
              // Release the permit. 
              System.out.println(threadName + " releases the permit."); 
              sem.release(); 
      } 
       
      // run by thread Y 
      else
      { 
          System.out.println("Starting " + threadName); 
          try
          { 
              // First, Y will try to get permit
              System.out.println(threadName + " waiting for a permit."); 
           
              // acquiring the lock 
              sem.acquire(); 
           
              System.out.println(threadName + " gets a permit."); 
       
              // Now, accessing the shared resource and others will wait
               
              for(int i=0; i < 7; i++) 
              { 
                  Resource.count--; 
                  System.out.println(threadName + ": " + Resource.count); 
       
                  // Now, allowing a context switch -- if possible. 
                  // for thread X to execute 
                  Thread.sleep(20); 
              } 
          } catch (InterruptedException exc) { 
                  System.out.println(exc); 
              } 
              // Release the permit. 
              System.out.println(threadName + " releases the permit."); 
              sem.release(); 
      } 
  } 
} 


public class SemTest 
{ 
  public static void main(String args[]) throws InterruptedException 
  { 
      // creating a Semaphore object 
      // with number of permits 1
      Semaphore sem = new Semaphore(1); 
       
      // creating two threads with name X and Y 
      // Here thread X will increment and Y will decrement the counter
      MyDemo md1 = new MyDemo(sem, "X"); 
      MyDemo md2 = new MyDemo(sem, "Y"); 
       
      // stating threads X and Y 
      md1.start(); 
      md2.start(); 
       
      // waiting for threads X and Y 
      md1.join(); 
      mtd.join(); 
       
   
      System.out.println("count: " + Resource.count); 
  } 
}
}
