package test;

public class Philosopher implements Runnable {

    private final Object leftFork;
    private final Object rightFork;

    public Philosopher(Object left, Object right) {
        this.leftFork = left;
        this.rightFork = right;
    }

    private void doAction(String action) throws InterruptedException {
        System.out.println(Thread.currentThread().getName() + " " + action);
        Thread.sleep(((int) (Math.random()*100)));
    }

    @Override
    public void run() {
        try {
            while(true) {
                doAction(System.nanoTime() + ":Thinking");
                synchronized (leftFork) {
                    doAction(System.nanoTime() + ": Picked up left");
                    synchronized (rightFork) {
                        doAction(System.nanoTime() + ": Picked up right fork and started to eat");
                        doAction(System.nanoTime() + ": Put down right fork");
                    }
                    doAction(System.nanoTime() + ": Put down left fork and returned to start thinking again");
                }
            }
        }
        catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
    public static void main(String[] args) throws Exception {

        Philosopher[] philosophers = new Philosopher[5];
        Object[] forks = new Object[philosophers.length];

        for (int i = 0; i < forks.length; i++) {
            forks[i] = new Object();
        }

        for (int j = 0; j < philosophers.length; j++) {
            Object leftFork = forks[j];
            Object rightFork = forks[(j+1) % forks.length];

            if (j == philosophers.length - 1) {
                philosophers[j] = new Philosopher(rightFork, leftFork);
            }
            else {
                philosophers[j] = new Philosopher(leftFork, rightFork);
            }
            Thread thread = new Thread(philosophers[j], "Philosopher " + (j+1));
            thread.start();

        }
    }
}
