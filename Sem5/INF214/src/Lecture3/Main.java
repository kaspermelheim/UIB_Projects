package Lecture3;

class Main {
	public static void main(String[] args) throws InterruptedException {
		try {
			//R, G, B
			Color c = new Color("green", 0, 255, 0);

			Thread t1 = new Thread() {
				public void run() {
					synchronized(c) {
						int value = c.getIntegerRepresentation();
						String name = c.getName();
						System.out.println(value);
						System.out.println(name);
					}
				};
			};

			Thread t2 = new Thread() {
				public void run() {
					synchronized(c) {
						c.set("red", 255, 0, 0);
					}
				};
			};

			t1.start();
			t2.start();
			t1.join();
			t2.join();
		}
		catch (InterruptedException e) {

		}
	}
}
