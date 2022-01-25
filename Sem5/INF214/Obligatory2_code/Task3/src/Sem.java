public class Sem {
	private int permits;

	public Sem(int permits) {
		this.permits = permits;
	}

	public synchronized void acquire() throws InterruptedException {
		if (permits <= 0) {
			while (permits <= 0) {
				wait();
			}
		}
		permits--;
	}

	public synchronized void release() {
		permits++;
		notify();
	}
}
